from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsletterSub, name='NewsletterSub'),
    path('mailmessage/', views.MailMessage, name='MailMessage')
]
