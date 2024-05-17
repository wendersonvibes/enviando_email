from django.urls import path

from .views.with_xhtml2pdf import GeneratePdf
from .views.index import index, curriculo, envia_email

urlpatterns = [
    path('', index, name='index'),
    path('envia-email/', envia_email, name='envia-email'),
    path('curriculo/', curriculo, name='curriculo'),

    # xhtml2pdf
    path('html-to-pdf/', GeneratePdf.as_view(), name='html-to-pdf'),

]




