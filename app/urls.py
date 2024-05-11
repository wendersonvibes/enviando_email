from django.urls import path
from . import views
from .views.with_reportlab import gerar_pdf

from .views.with_xhtml2pdf import GeneratePdf, curriculo

from .views.with_pdfkit import page, pdfkit_generate

from .views import index

urlpatterns = [
    path('', index.index, name='index'),
    path('envia-email/', index.envia_email, name='envia-email'),
    path('gerar-pdf/', gerar_pdf, name='gerar-pdf'),
    path('curriculo/', curriculo, name='curriculo'),
    path('html-to-pdf/', GeneratePdf.as_view(), name='html-to-pdf'),

    # pdfkit
    path('page', page, name='page'),
    path('pdfkit-generate/', pdfkit_generate, name='pdfkit-generate'),
]




