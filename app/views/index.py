import json

from django.shortcuts import render, redirect
from django.core.mail import send_mail

from app.utils.api_cep import buscar_cep

def curriculo(request):
    return render(request, "pdf/curriculo.html")

def index(request):
    context = {}
    if request.method == 'POST':
        cep = request.POST['cep']
        cep_response = buscar_cep(cep)

        response = json.loads(cep_response)
        context['response'] = response
        
    return render(request, "index.html", context)

def envia_email(request):
    send_mail('Assunto', 'Email enviado com sucesso', 'wenderson1909@gmail.com', ['wenderbully.1234@gmail.com'])
    return redirect('index')


