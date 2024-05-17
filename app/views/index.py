from django.shortcuts import render, redirect
from django.core.mail import send_mail

def curriculo(request):
    return render(request, "pdf/curriculo.html")

def index(request):
    return render(request, "index.html")

def envia_email(request):
    send_mail('Assunto', 'Email enviado com sucesso', 'wenderson1909@gmail.com', ['wenderbully.1234@gmail.com'])
    return redirect('index')


