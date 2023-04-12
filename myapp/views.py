from django.shortcuts import redirect, render
from time import sleep
# Create your views here.
from .helper import *
from django.http import HttpResponse
from .task import *
def home(requset):
    return HttpResponse("Hello from celery")

def mail_send(requset):
    send_mail_task.delay()
    return HttpResponse("Mail Sent")

def mail_to_all(requset):
    send_mail_to_all.delay()
    return HttpResponse("Mail Sent To All")