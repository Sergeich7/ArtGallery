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
        if self.kwargs.get('pk'):
            prod = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        else:
            prod = get_object_or_404(Product, slug=self.kwargs.get('slug'))
        context['product'] = prod
        context['thumb1st'] = prod.thumbnail.picture
        context['thumbs_wo_1st'] = prod.images.exclude(id=prod.thumbnail.id)
        context['all_comments'] = ArtComment.objects.filter(product=prod.pk)
        return context
# може так быстрее чем через вычисляемое поле?
#        if not th:
#            th = prod.images.order_by('?').first()
#        context['product'] = prod
#        context['thumb1st'] = th.picture
#        context['thumbs_wo_1st'] = prod.images.exclude(id=th.pk)
#        context['all_comments'] = ArtComment.objects.filter(product=prod.pk)
#        return context

    def get_success_url(self):
        """Возврат на ту-же страницу после добавления комментария."""
        if self.kwargs.get('pk'):
            args = (self.kwargs.get('pk'), )
        else:
            args = (self.kwargs.get('slug'),)
        return reverse('art:detail', args=args) + \
            '#comments'

    def form_valid(self, form):
        """Добавляем пользователя (комментатора) в форму."""
        form.instance.user = self.request.user
        if self.kwargs.get('pk'):
            form.instance.product = Product.objects.get(pk=self.kwargs.get('pk'))
        else:
            form.instance.product = Product.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """Удаляем комментарий на текущей странице если нужно."""
        if kwargs.get("dc"):
            # удаляем комментарий
            cm = ArtComment.objects.filter(id=kwargs.get("dc"))
            cm.delete()
        return super().get(request, *args, **kwargs)
