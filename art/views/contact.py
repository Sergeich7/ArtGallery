from xml.dom.minidom import Attr
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django import forms

from captcha.fields import CaptchaField, CaptchaTextInput

from project.settings import ADMIN


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'Ваше имя',}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={"class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'e-mail',}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": "4", "class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'Текст сообщения',}))
    captcha = CaptchaField(
        label='',
        error_messages={'invalid': 'Неправильный текст'},
        widget=CaptchaTextInput(attrs={"class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'Введите текст с картинки',})
        )


class ContactFormView(FormView):
    """Контакты владельца и обратная связь."""

    template_name = 'art/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('art:thanks')

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

