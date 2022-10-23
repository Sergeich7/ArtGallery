from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django import forms

from captcha.fields import CaptchaField, CaptchaTextInput

from project.settings import ADMIN

from ..models import Author, Category


class ContactForm(forms.Form):

    to = forms.ChoiceField(
        required=True,
        label='',
        widget=forms.Select(attrs={"class": "rounded-0 w-100 input-area name, mb-4", })
    )

    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'Ваше имя',}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={"class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'e-mail',}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": "4", "class": "rounded-0 w-100 input-area name, mb-4", 'placeholder': 'Текст сообщения',}))
    captcha = CaptchaField(
        label='',
        error_messages={'invalid': 'Неправильный текст с картинки'},
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        to_choices =[
            (None, "Выберете получателя"),
            ("adm", "Администрация сайта"),
        ]
        [to_choices.append((a.pk, str(a)),) for a in Author.objects.all()]
        self.fields['to'].choices = to_choices
        if kwargs.get('data'):
            captcha_placeholder = 'Неверно введен текст с картинки. Повторите. '
        else:
            captcha_placeholder = 'Введите текст с картинки'
        self.fields['captcha'].widget = CaptchaTextInput(attrs={
            "class": "rounded-0 w-100 input-area name, mb-4",
            'placeholder': captcha_placeholder, })


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
        to_id = self.request.POST.get('to', '')
        if type(to_id) == int:
            # отправляем письмо автору работа
            to_emails = [Author.objects.get(pk=to_id).email, ]
        else:
            # отправляем письмо админам
            to_emails = [e for _, e in ADMIN]
        send_mail(
            'artgallery-tatyana.ru - contact form',     # тема
            message,                # тело
            f'{name} <{email}>',    # отправитель
            to_emails,              # получатели
            fail_silently=False,
        )
        return super().form_valid(form)

