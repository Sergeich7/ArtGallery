from django.views.generic import CreateView
from django.urls import reverse
from django import forms

from art.models import Product, ArtComment
from art.views import AddContextMixin


class CommentForm(forms.ModelForm):

    class Meta:
        model = ArtComment
        fields = ('text',)      # отображать только поле для ввода текста
        labels = {                  # не отображать для него заголовок
            'text': '',
        }


class DetailView(AddContextMixin, CreateView):
    model = ArtComment
    template_name = 'art/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_cat = Product.objects.get(pk=self.kwargs.get('pk')).category.id
        context['product'] = Product.objects.get(pk=self.kwargs.get('pk'))
        context['all_comments'] = ArtComment.objects.filter(
            product=self.kwargs.get('pk'))
        return self.add_context(context, active_cat=active_cat)

    def get_success_url(self):
        """Возврат на ту-же страницу после добавления комментария."""
        return reverse('art:detail', args=(self.kwargs.get('pk'))) + \
            '#comments'

    def form_valid(self, form):
        """Добавляем пользователя (комментатора) в форму."""
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """Удаляем комментарий на текущей странице если нужно."""
        if kwargs.get("dc"):
            # удаляем комментарий
            cm = ArtComment.objects.filter(id=kwargs.get("dc"))
            cm.delete()
        return super().get(request, *args, **kwargs)
