from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django import forms

from captcha.fields import CaptchaField

from project.settings import ADMIN
from art.views import AddContextMixin


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField(
        label='Введите текст с картинки',
        error_messages={'invalid': 'Неправильный текст'}
        )


class ContactFormView(AddContextMixin, FormView):
    """Контакты владельца и обратная связь."""

    template_name = 'art/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('art:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context)

    def form_valid(self, form):
        """Отправка письма владельцу сайта, если форма валидна."""
        name = self.request.POST.get('name', '')
        email = self.request.POST.get('email', '')
        message = self.request.POST.get('message', '')
        send_mail(
            'artgallery-tatyana.ru - contact form',     # тема
            message,                    # тело
            f'{name} <{email}>',        # отправитель
            [e for _, e in ADMIN],      # получатель - все админы
            fail_silently=False,
        )
        return super().form_valid(form)

