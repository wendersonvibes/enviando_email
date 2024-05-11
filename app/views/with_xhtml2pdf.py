from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.utils import render_to_pdf

from .index import send_email_with_attachment

def curriculo(request):
    return render(request, "pdf/curriculo.html")

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {}
        data['idade'] = [21, 12]
        pdf = render_to_pdf('pdf/curriculo.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')

        subject = "Currículo"
        message = "Consegui, Anael"
        recipient_list = ['wenderbully.1234@gmail.com', 'anael.b@escolar.ifrn.edu.br']

        send_email_with_attachment(subject, message, recipient_list, response)
        return response