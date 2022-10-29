from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django import forms

from art.models import Product, ArtComment


class CommentForm(forms.ModelForm):

    class Meta:
        model = ArtComment
        fields = ('text',)      # отображать только поле для ввода текста
        labels = {                  # не отображать для него заголовок
            'text': '',
        }
        widgets = {
            "text": forms.Textarea(attrs={'cols': '30', 'rows': '5', 'class': 'rounded-0 w-100 custom-textarea input-area',}),
        }  


class DetailView(CreateView):
    model = ArtComment
    template_name = 'art/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prod = Product.objects.filter(slug=self.kwargs.get('slug')).\
            select_related('author', 'category', 'technique', 'th_of_day').\
            only(
                'id',
                'title',
                'created',
                'description',
                'materials',
                'size',
                'author_id',
                'category_id',
                'technique_id',
                'th_of_day',

                'author__id',
                'author__last_name',
                'author__first_name',
                'author__patronymic',

                'category__id',
                'category__title',
                'technique__id',
                'technique__title',
            ).first()
        context['product'] = prod
        context['thumbs_wo_1st'] = prod.images.exclude(id=prod.th_of_day.pk)
        context['vids'] = prod.videos.all()
        context['all_comments'] = ArtComment.objects.filter(product=prod.pk)
        return context

    def get_success_url(self):
        """Возврат на ту-же страницу после добавления комментария."""
        args = (self.kwargs.get('slug'),)
        return reverse('art:detail', args=args) + \
            '#comments'

    def form_valid(self, form):
        """Добавляем пользователя (комментатора) в форму."""
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """Удаляем комментарий на текущей странице если нужно."""
        if kwargs.get("dc"):
            # удаляем комментарий
            cm = ArtComment.objects.filter(id=kwargs.get("dc"))
            cm.delete()
        return super().get(request, *args, **kwargs)
