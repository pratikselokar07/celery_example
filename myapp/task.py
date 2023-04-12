from celery import shared_task
import time
from django.core.mail import send_mail
from .models import Student
from celery_example import settings
# @shared_task
# def handle_sleep():
#     print('Handle sleep started')
#     time.sleep(10)

@shared_task
def send_mail_task():
    send_mail('Celery Worked', 'Celery Done with Email',
              'pratikselokar02@gmail.com',
              ['pratikselokar07@gmail.com'],
              fail_silently=False
              )
    return "Done"

@shared_task(name='myapp.tasks.send_mail_to_all')
def send_mail_to_all():
    users=Student.objects.all()
    for user in users:
        mail_subject ="Hi! Celery Testing"
        message="Hi! this is Pratik "
        to_mail=user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True
        )
    return "Done"