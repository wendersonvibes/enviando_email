import json
from django.http import HttpResponse
from django.views.generic import View

from app.utils.functions import render_to_pdf, send_email_with_attachment
from app.utils.api_cep import buscar_cep

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {}
        data['idade'] = [21, 12]

        cep_response = buscar_cep(59270000)
        response = json.loads(cep_response)
        data['response'] = response

        pdf = render_to_pdf('pdf/curriculo.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')

        subject = "Currículo"
        message = "Consegui, Anael"
        recipient_list = ['wenderbully.1234@gmail.com']

        send_email_with_attachment(subject, message, recipient_list, response)
        return response