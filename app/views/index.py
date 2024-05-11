from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.core.mail import send_mail, EmailMessage

from django.conf import settings

def index(request):
    return render(request, "index.html")

def send_email_with_attachment(subject, message, recipient_list, file):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach(filename="curriculo.pdf", content=file.content, mimetype="application/pdf")
    mail.send()

def envia_email(request):
    send_mail('Assunto', 'Email enviado com sucesso', 'wenderson1909@gmail.com', ['wenderbully.1234@gmail.com'])
    return redirect('index')


