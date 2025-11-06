from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.urls import reverse


def inicio_taller(request):
    # página principal de la app (taller)
    return render(request, 'inicio.html', {})

def agregar_clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        email = request.POST.get('email', '').strip() or None
        rfc = request.POST.get('rfc', '').strip() or None
        telefono = request.POST.get('telefono', '').strip() or None
        direccion = request.POST.get('direccion', '').strip() or None
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            rfc=rfc,
            telefono=telefono,
            direccion=direccion,
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_clientes.html', {})

def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        email = request.POST.get('email', '').strip()
        cliente.email = email or None
        rfc = request.POST.get('rfc', '').strip()
        cliente.rfc = rfc or None
        telefono = request.POST.get('telefono', '').strip()
        cliente.telefono = telefono or None
        direccion = request.POST.get('direccion', '').strip()
        cliente.direccion = direccion or None
        cliente.save()
        return redirect('ver_clientes')
    # si llama GET, redirigir a formulario de edición
    return redirect('actualizar_clientes', cliente_id=cliente.id)

def borrar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})