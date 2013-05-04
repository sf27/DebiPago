#-*- encoding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', 'tienda_app.views.index', name='index'),
    #url( r'^articles/(?P<query>\w+)$', 'tienda_app.views.ajax_user_search', name = 'demo_user_search' ),
    
    url(r'^compra/$', 'tienda_app.views.compra_ajax', name='compra_ajax'),
    url(r'^comentario/$', 'tienda_app.views.comentario_ajax', name='comentar_ajax'),
    url(r'^articulo/(?P<id_articulo>\d+)$', 'tienda_app.views.articulo', name="articulo"),
    url(r'^categoria/(?P<categoria>\w+)/articulos/$','tienda_app.views.buscar_articulos', name="buscar_articulos"),
    url(r'^categorias_ajax/$', 'tienda_app.views.buscar_articulos_ajax', name="busqueda"),
    url(r'^load_c/$', 'tienda_app.views.load_comments', name="load_comments"),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
)
