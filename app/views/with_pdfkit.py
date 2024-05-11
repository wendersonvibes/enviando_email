from django.urls import reverse
import pdfkit

from django.shortcuts import render
from django.http import HttpResponse

config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

def page(request):
    return render(request, "pdf_pdfkit/pdf.html")

def pdfkit_generate(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('page')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="file_name.pdf"'

    return response

