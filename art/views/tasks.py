from project.celery import app
from django.core.mail import send_mail


@app.task
def send_mail_to_one(
        mail_from, mail_to, mail_title, mail_body, mail_body_html: str
        ) -> bool:

    mail_to = (mail_to,)
    
    # Отправляем письмо
    return send_mail(
        mail_title,
        mail_body,
        mail_from,
        mail_to,
        fail_silently=False,
        html_message=mail_body_html
    )
