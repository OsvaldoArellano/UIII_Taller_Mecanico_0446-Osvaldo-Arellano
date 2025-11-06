from django.contrib import admin
from .models import Cliente, Servicio, Vehiculo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'rfc', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email', 'rfc')


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_base', 'tiempo_est', 'aplica_garantia', 'fecha_actualizacion')
    search_fields = ('nombre',)


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'modelo', 'anio', 'cliente')
    search_fields = ('matricula', 'marca', 'modelo')