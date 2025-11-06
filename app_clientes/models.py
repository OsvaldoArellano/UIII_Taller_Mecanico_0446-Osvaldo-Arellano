from django.db import models

# MODELO: Cliente (taller)
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# MODELO: Servicio (reemplaza viajes/transporte conceptualmente)
class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tiempo_est = models.IntegerField(help_text='Tiempo estimado en minutos', default=0)
    aplica_garantia = models.BooleanField(default=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


# MODELO: Vehiculo
class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, blank=True, null=True, related_name='vehiculos')
    matricula = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField(blank=True, null=True)
    kilometraje = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.modelo}"