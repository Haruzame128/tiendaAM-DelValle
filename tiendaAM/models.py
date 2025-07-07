from django.db import models

# Modelos para la aplicacion Tienda AM 
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

class Productos(models.Model):
    TIPO_CHOICES = [
        ('ropa', 'Ropa'),
        ('armas', 'Armas'),
        ('accesorios', 'Accesorios'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    tipo_producto = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
    
class Escuelas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre