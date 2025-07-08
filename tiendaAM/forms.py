from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label='Nombre del Producto')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    stock = forms.IntegerField(label='Stock')
    tipo_producto = forms.ChoiceField(choices=[
        ('ropa', 'Ropa'),
        ('armas', 'Armas'),
        ('accesorios', 'Accesorios')
    ], label='Tipo de Producto')

class EscuelaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre de la Escuela')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    ubicacion = forms.CharField(max_length=200, label='Ubicación')