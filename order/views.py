from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from .models import Order, OrderItem
from weasyprint import HTML
from io import BytesIO

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = Order.objects.get(id=order_id)
        order_items = sorted(OrderItem.objects.filter(order=order), key=lambda item: item.product.name )
        total_amount = sum([
            item.product.price * item.quantity 
            for item in order_items 
            if not item.leased_equipment
        ])
        has_leased_equipment = any(item.leased_equipment for item in order_items)

        company = request.user.company
        print(request.user.company.owner)
        # Renderiza o template HTML com os dados
        context = {
            'order': order,
            'order_items': order_items,
            'total_amount': total_amount,
            'has_leased_equipment': has_leased_equipment,
            'company': company,
        }
        template = get_template('template.html')
        html_content = template.render(context)

        # Converte o HTML para PDF usando WeasyPrint
        pdf_file = HTML(string=html_content).write_pdf()

        # Cria uma resposta HTTP com o conteúdo do PDF
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="orcamento.pdf"'

        return response
