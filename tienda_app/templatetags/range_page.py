#-*- encoding:utf-8 -*-
# tienda_web/tienda_app/template_tags/range_page.py
# website/app/template_tags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='range') 
def times(number):
    number = int(1 if number is None else number)
    return range(1, number+1)

@register.filter(name='to_int')   
def to_int(type_data):
    return int(1 if type_data is None else type_data)
