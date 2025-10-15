from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

# Create your views here.

# Listar empleados
def index(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

# Ver empleado (opcional, puedes usarlo si quieres detalle)
def ver_empleados(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'ver_empleados.html', {'empleado': empleado})

# Agregar empleado
def agregar_empleados(request):
    if request.method == 'POST':
        nombre_empleado = request.POST['nombre_empleado']
        apellido_empleado = request.POST['apellido_empleado']
        rfc_empleado = request.POST['rfc_empleado']
        puesto_empleado = request.POST['puesto_empleado']
        contratacion_empleado = request.POST['contratacion_empleado']
        Empleado.objects.create(nombre_empleado=nombre_empleado, apellido_empleado=apellido_empleado, rfc_empleado=rfc_empleado, puesto_empleado=puesto_empleado, contratacion_empleado=contratacion_empleado )
        return redirect('inicio')
    return render(request, 'agregar_empleados.html')

# Editar empleado
def editar_empleados(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre_empleado = request.POST['nombre_empleado']
        empleado.apellido_empleado = request.POST['apellido_empleado']
        empleado.rfc_empleado = request.POST['rfc_empleado']
        empleado.puesto_empleado = request.POST['puesto_empleado']
        empleado.contratacion_empleado = request.POST['contratacion_empleado']
        empleado.save()
        return redirect('inicio')
    return render(request, 'editar_empleados.html', {'empleado': empleado})

# Borrar empleado
def borrar_empleados(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio')
    return render(request, 'borrar_empleados.html', {'empleado': empleado})