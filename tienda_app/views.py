#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from tienda_app.models import Articulo, Categoria, Comentario, Compra
from tienda_app.forms import searchForm 
from django.utils import simplejson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from tienda_app.utils.format_date import apply

def index(request):
    a = Articulo.objects.filter(cantidad__gte=1)#articulos con cantidad disponible
    if request.method == "GET":
        form = searchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            a = Articulo.objects.filter(nombre__icontains=query, cantidad__gte=1)
    paginator = Paginator(a, 3) # Show 25 articulos per page
    page = request.GET.get('page')
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    
    return render_to_response('tienda/index.html', {'articulos':articulos, "formulario":searchForm()}, context_instance=RequestContext(request))


def articulo(request, id_articulo):
    a = get_object_or_404(Articulo, pk=id_articulo)#articulo
    c = Comentario.objects.filter(articulo=a).order_by('fecha_registro').reverse()#comentarios
    paginator = Paginator(c, 3)
    page = request.GET.get('page', 1)
    try: 
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    if request.method == "GET":
        form = searchForm(request.GET)
        if form.is_valid(): 
            query = form.cleaned_data['query']
            if query:#si tiene datos, entonces hace la busqueda
                a = Articulo.objects.filter(nombre__icontains=query, cantidad__gte=1)#consulta si contiene algun registro con la query y que contengan cantidad disponible
                return render_to_response('tienda/index.html', {'articulos':a, "formulario":searchForm()}, context_instance=RequestContext(request))
    return render_to_response('tienda/articulo.html', {'articulo':a, 'comentarios': comments, "formulario":searchForm()}, context_instance=RequestContext(request))
   
 
def buscar_articulos(request, categoria):
    c = Categoria.objects.get(nombre=categoria)#obtiene el objeto categoria
    a = Articulo.objects.filter(cantidad__gte=1, categoria=c)#obtiene la lista de articulos de esa categoria y que tengan cantidad disponible
    #campo de busqueda
    if request.method == "GET":
        form = searchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:#si tiene datos, entonces hace la busqueda
                a = Articulo.objects.filter(nombre__icontains=query, cantidad__gte=1)#consulta si contiene algun registro con la query y tengan cantidad disponible
    paginator = Paginator(a, 3) # Show 25 articulos per page
    page = request.GET.get('page')
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    return render_to_response('tienda/index.html', {'articulos':articulos, "formulario":searchForm()}, context_instance=RequestContext(request))



def buscar_articulos_ajax(request):
    if request.is_ajax():
        a = Articulo.objects.filter(cantidad__gte=1)#articulos con cantidad disponible
        data = [i.nombre for i in a]
    else:    
        data = "Error, peticion no procesada"      
    json = simplejson.dumps(data) 
    return HttpResponse(json, mimetype='application/json') 


def compra_ajax(request): 
    if request.is_ajax():  
        cantidad_vendida = int(request.GET.get('cantidad'))
        precio_actual = float(request.GET.get('precio'))
        id_articulo = int(request.GET.get('id'))
        a = get_object_or_404(Articulo, pk=id_articulo)#articulo
        cant = a.cantidad
        if cantidad_vendida >= cant:
            a.cantidad = 0
        else:  
            a.cantidad = a.cantidad - cantidad_vendida#se restan la cantidad comprada
        a.save()#se guarda el registro
        ####################################################################
        user_c = User.objects.get(pk=1)#se debe obtener el usuario logueado    
        Compra.objects.create(cantidad=cantidad_vendida, precio_articulo=precio_actual, status='En proceso', articulo=a, usuario=user_c)
        return HttpResponseRedirect('/')  
    return HttpResponseRedirect('/')#sino es una peticion ajax, redirecciona al home   
 

def comentario_ajax(request): 
    if request.is_ajax():  
        if request.method == 'POST':
            c =  request.POST.get('comentario')
            id_a = request.POST.get('id_articulo')
            ####################################################################
            a = get_object_or_404(Articulo, pk=id_a)#articulo 
            #print request.user
            user_c = User.objects.get(pk=1)#se debe obtener el usuario logueado   
            Comentario.objects.create(contenido=c, articulo=a, usuario=user_c)            
            return redirect('/')          
    return redirect('/')#sino es una peticion ajax, redirecciona al home  


def load_comments(request): 
    if request.is_ajax(): 
        if request.method == 'POST':  
            id_a = request.POST.get('id_articulo')
            number_page = int(request.POST.get('number_page')) 
            ####################################################################
            a = Articulo.objects.get(pk=id_a)
            list_c = Comentario.objects.filter(articulo=a).order_by("fecha_registro").reverse()
            # Get the paginator
            #apply the timezone
            from pytz import timezone
            from tienda_web.settings import TIME_ZONE
            tz1=timezone(TIME_ZONE)
            paginator = Paginator(list_c, 3)         
            try:                      
                #import pdb; pdb.set_trace()
                comments = paginator.page(number_page)
                coms = [str(i.contenido) for i in comments]
                fech = [apply(i.fecha_registro.astimezone(tz1)) for i in comments] 
                #fech = map(apply, [i.fecha_registro.astimezone(tz1) for i in comments])  
                l = zip(coms, fech) 
                l.append([number_page+1])  #el ultimo arrays es el numero de pagina
                json = simplejson.dumps(l) #arrays de arrays [[], [], []]
            except (EmptyPage, InvalidPage):
                json = simplejson.dumps(False)##retorna False para indicar que no hay mas paginacion
            return HttpResponse(json, mimetype='application/json')
        return redirect('/')              
    return redirect('/')#sino es una peticion ajax, redirecciona al home  
    














