from django.forms import ModelForm
from django import forms
from tienda_app.models import Compra

class searchForm(forms.Form):
    query = forms.CharField(label='Busqueda', min_length=3, required=False)
       
class compraForm(ModelForm):
    class Meta:
        model = Compra