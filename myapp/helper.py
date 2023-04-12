from django.core.mail import send_mail

def send_mail_without_celery():
    send_mail('Celery Worked', 'Celery',
              'pratikselokar02@gmail.com',
              ['pratikselokar07@gmail.com'],
              fail_silently=False
              )
    return None
