from django.urls import path

from .views import *

urlpatterns = [
     path('',home),
     path('send_mail',mail_send),
     path('send_mail_to_all',mail_to_all),
]
