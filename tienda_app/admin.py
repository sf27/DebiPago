from tienda_app.models import Articulo, Categoria, Comentario, Compra
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_registro')
    list_filter  = ['fecha_registro']
    search_fields = ['nombre']
    date_hierarchy = 'fecha_registro'
    

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'precio', 'cantidad', 'usuario')
    list_filter  = ['fecha_registro']
    search_fields = ['nombre']
    date_hierarchy = 'fecha_registro'
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'fecha_registro', 'articulo', 'usuario')
    list_filter  = ['fecha_registro']
    search_fields = ['contenido']
    date_hierarchy = 'fecha_registro'
    
class CompraAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'cantidad', 'precio_articulo', 'status', 'fecha_registro', 'usuario')
    list_filter  = ['fecha_registro']
    search_fields = ['articulo']
    date_hierarchy = 'fecha_registro'

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Compra, CompraAdmin)