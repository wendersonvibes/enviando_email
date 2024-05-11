import io
from django.http import FileResponse
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph
from django.template.loader import render_to_string
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table, TableStyle

# Estilos padrões
styles = getSampleStyleSheet()

# Estilos personalizados
justificar = ParagraphStyle('justificar', 
    fontSize=12,
    alignment=4, # 4 para justificar
    leading=18,
    spaceBefore=15,
)

def gerar_pdf(request):
    width, height = A4
    wrapX = 420
    drawX = width - 500

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Cria o arquivo PDF, usando o "buffer" como um arquivo
    c = canvas.Canvas(buffer, pagesize=letter)

    # Título 1
    titulo_1 = Paragraph("1. Apresentação", styles['Heading1'])
    titulo_1.wrapOn(c, wrapX, 100) # Definir as margens do texto
    titulo_1.drawOn(c, drawX, height-150)

    # Parágrafo
    paragrafo_1 = Paragraph("""A Renova Solar está pavimentando um caminho de conquistas, elas contam com a confiança de nossos fornecedores, colaboradores e sobretudo, clientes. Prezamos pela preferência através de muito compromisso e trabalho. O nosso ideal mercadológico hoje é possibilitar o fornecimento de energia observando as diretrizes de melhor custo-benefício, agilidade e autossustentabilidade""", justificar)
    paragrafo_1.wrapOn(c, wrapX, 50)
    paragrafo_1.drawOn(c, drawX, height-250)

    # Tabela
    dados = [['a', 'b'],
             ['c', 'd'],
             ['e', 'f']]
    
    tabela = Table(dados)

    # Close the PDF object cleanly, and we're done.
    c.setTitle("Relatório") # Nome do documento
    c.showPage() 
    c.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename="hello.pdf")