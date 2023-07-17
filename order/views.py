from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from .models import Order, OrderItem
from django.conf import settings
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import StringIO
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
# from reportlab.graphics.renderers import SvgRenderer


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)

        # Create a response object with PDF content type
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="orcamento.pdf"'

        # Create a PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Set up styles
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        description_style = styles['Heading2']
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),  # Header background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ])

        row_colors = [colors.white, colors.Color(0.9, 0.9, 0.9)]
        for i in range(1, len(order_items)):
            row_color = row_colors[i % len(row_colors)]
            table_style.add('BACKGROUND', (0, i), (-1, i), row_color)

        table_style.add('GRID', (0, 0), (-1, -1), 1, colors.black)

        # Create story elements
        story = []

        drawing = svg2rlg('order/static/logo.svg')
        story.append(drawing)
        # renderPDF.drawToFile(drawing, output_path)
        # renderPM.drawToFile(drawing, 'svg_demo.png', 'PNG')


        company_info = [
            ['Inviosat Monitoramento'],
            ['Avenida Antonio Silvio Barbierri 2346'],
            ['Fone: 46 35344248 | 46 999800080'],
            ['CNPJ: 10.243.551/0001-30']
        ]
        company_table = Table(company_info, colWidths=[400])
        company_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')]))
        story.append(company_table)

        # Add customer information
        customer_info = [
            ['Data de emissão:', f'{order.created_at.strftime("%A, %B %d, %Y")}'],
            ['Nome:', f'{order.customer.name}', 'Cpf/Cnpj:', f'{order.customer.cpf_cnpj}'],
            ['Bairro:', 'Rua:', 'n°:', ''],
            ['Cep:', '']
        ]
        customer_table = Table(customer_info, colWidths=[80, 200, 80, 200])
        customer_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')]))
        story.append(customer_table)
        story.append(Spacer(1, 20))

        # Add order description table
        data = [['DESCRIÇÃO', 'QUANTIDADE', 'VALOR UNT.', 'TOTAL']]
        total_amount = 0
        for item in order_items:
            data.append([item.product.name, item.quantity, f'R$ {item.product.price:.2f}', f'R$ {item.quantity * item.product.price:.2f}'])
            total_amount += item.quantity * item.product.price
        table = Table(data, colWidths=[300, 80, 100, 100])
        table.setStyle(table_style)
        story.append(table)
        story.append(Spacer(1, 20))

        # Add total amount
        total_paragraph = f'TOTAL: R$ {total_amount:.2f}'
        total_paragraph = Paragraph(total_paragraph, header_style)
        story.append(total_paragraph)

        # Build the PDF document
        doc.build(story)

        return response
