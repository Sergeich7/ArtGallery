from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django import forms

from captcha.fields import CaptchaField, CaptchaTextInput

from project.settings import ADMIN

from ..models import Author
from .tasks import send_mail_to_one


class ContactForm(forms.Form):

    to = forms.ChoiceField(
        required=True,
        label='',
        widget=forms.Select(
            attrs={"class": "rounded-0 w-100 input-area name, mb-4", })
    )

    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "class": "rounded-0 w-100 input-area name, mb-4",
            'placeholder': 'Ваше имя', }))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            "class": "rounded-0 w-100 input-area name, mb-4",
            'placeholder': 'e-mail', }))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        "rows": "4", "class": "rounded-0 w-100 input-area name, mb-4",
        'placeholder': 'Текст сообщения', }))
    captcha = CaptchaField(
        label='',
        error_messages={'invalid': 'Неправильный текст с картинки'},)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Список для выбора получателя
        to_choices = [
            (None, "Выберете получателя"),
            ("adm", "Администрация сайта"),
        ]
        for a in Author.objects.all().exclude(contacts_off=True).\
                only('last_name', 'first_name', 'patronymic'):
            to_choices.append((a.pk, str(a)),)

        self.fields['to'].choices = to_choices
        if kwargs.get('data'):
            captcha_placeholder = 'Неверно введен текст с картинки. Повторите.'
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
        """Отправка письма владельцам сайта или авторам, если форма валидна."""

        name = self.request.POST.get('name', '')
        email = self.request.POST.get('email', '')

        mail_title = f'artgallery-tatyana.ru contact form {name} {email}'
        mail_body = self.request.POST.get('message', '')
        mail_body_html = mail_body
        mail_from = 'artgallery-tatyana.ru <pl3@yandex.ru>'

        to_id = self.request.POST.get('to', '')
        if type(to_id) == int:
            # отправляем письмо автору работа
            to_emails = [Author.objects.get(pk=to_id).email, ]
        else:
            # отправляем письмо админам
            to_emails = [e for _, e in ADMIN]
        for mail_to in to_emails:
            # Запускаем задачу отправку одного письма
            # отложенную на 0 (countdown=0) сек
            send_mail_to_one.apply_async(
                (
                    mail_from,
                    mail_to,
                    mail_title,
                    mail_body,
                    mail_body_html,
                ),
                countdown=0)

#        name = self.request.POST.get('name', '')
#        email = self.request.POST.get('email', '')
#        message = self.request.POST.get('message', '')
#        to_id = self.request.POST.get('to', '')
#        if type(to_id) == int:
#            # отправляем письмо автору работа
#            to_emails = [Author.objects.get(pk=to_id).email, ]
#        else:
#            # отправляем письмо админам
#            to_emails = [e for _, e in ADMIN]
#        send_mail(
#            f'artgallery-tatyana.ru contact form {name} {email}',     # тема
#            message,                # тело
#            'artgallery-tatyana.ru <pl3@yandex.ru>', # отправитель
#            to_emails,              # получатели
#            fail_silently=False,
#        )

        return super().form_valid(form)
