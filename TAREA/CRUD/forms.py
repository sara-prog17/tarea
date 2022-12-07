from django.forms import ModelForm,DateInput, TimeInput,Select,TextInput,NumberInput
from .models import Cliente, Pedido

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': TextInput (attrs={'class': 'form-control'}),
            'apellido': TextInput (attrs={'class': 'form-control'}),
            'f_nacimiento': DateInput(attrs={'type':'date','class':'form-control'}),
            'f_exp_documento': DateInput(attrs={'type':'date','class':'form-control'}),
            'documento': NumberInput (attrs={'class': 'form-control','max':9999999999}),
            'edad': NumberInput (attrs={'class': 'form-control','max':99}),
            'genero': TextInput (attrs={'class': 'form-control'}),
            'l_exp_documento': TextInput (attrs={'class': 'form-control'}),
            'ciud_residencia': TextInput (attrs={'class': 'form-control'}),
            'celular': NumberInput (attrs={'class': 'form-control','max':9999999999}),
        }
        labels = {'f_nacimiento': 'Fecha de nacimiento', 'f_exp_documento': 'Fecha de expedición del documento','l_exp_documento':'Lugar expedición del documento','ciud_residencia': 'ciudad de residencia'}
        
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'cliente': Select (attrs={'class':'form-control'}),
            'tiempo_entrega':TimeInput(attrs={'type':'time', 'class':'form-control'}),
            'n_pedido': TextInput (attrs={'class': 'form-control'}),
            'productos': TextInput (attrs={'class': 'form-control'}),
            'valor_producto': TextInput (attrs={'class': 'form-control'}),
            'producto_mas_transporte': TextInput (attrs={'class': 'form-control'}),
            'tamaño_producto': TextInput (attrs={'class': 'form-control'}),
            'incremento': TextInput (attrs={'class': 'form-control'}),
            'proveedor': TextInput (attrs={'class': 'form-control'}),
            'cantidad_productos': TextInput (attrs={'class': 'form-control'}),
        }
        labels = {'n_pedido': 'Número de pedido',
        'valor_producto': 'Valor del Producto a transportar',
        'producto_mas_transporte':'Valor del producto más el transporte',
        'tamaño_producto':'Tamaño del producto'}
