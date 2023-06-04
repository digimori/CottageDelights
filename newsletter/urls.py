from django.urls import path
from . import views

urlpatterns = [
    path('', views.Newsletter, name='Newsletter'),
    path('', views.MailMessage, name='MailMessage')
]
