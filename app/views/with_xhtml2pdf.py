from django.http import HttpResponse
from django.views.generic import View

from app.utils.functions import render_to_pdf, send_email_with_attachment

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {}
        data['idade'] = [21, 12]

        pdf = render_to_pdf('pdf/curriculo.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')

        subject = "Currículo"
        message = "Consegui, Anael"
        recipient_list = ['wenderbully.1234@gmail.com']

        send_email_with_attachment(subject, message, recipient_list, response)
        return response