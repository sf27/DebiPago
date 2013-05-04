from django import template

from tienda_app.models import Categoria

register = template.Library()

@register.inclusion_tag('tienda/lista_categorias.html', takes_context=True)
def load_categories(context):
	categorias = Categoria.objects.all().order_by('-id')
	return {'categorias': categorias}
