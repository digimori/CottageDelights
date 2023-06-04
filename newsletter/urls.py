from django.urls import path
from . import views

urlpatterns = [
    path('', views.Newsletter, name='Newsletter'),
    path('mailmessage/', views.MailMessage, name='MailMessage')
]
