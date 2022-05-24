from django.shortcuts import render
from .models import notificacion , residente
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactoForm ,NotificacionForm, ResidenteForm
# Create your views here.



def home (request):
    notificaciones =notificacion.objects.all()
    data ={
        'notificaciones' :notificaciones
    }
    return render(request , 'app/home.html', data)

def directiva(request):
    return render(request,'app/directiva.html')

def residentes (request):
    return render(request , 'app/residente.html')

def contactos (request):
    data={
        'form':ContactoForm()
    }
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data[ "mensaje"]="mensaje guardado"
        else:
            data[ "form"]=formulario

    return render(request , 'app/contacto.html',data)

def agregar_notificacion(request):
    data={
        'form':NotificacionForm()
    }
    if request.method=='POST':
        formulario =NotificacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data[ "mensaje"]="mensaje guardado"
        else:
            data[ "form"]=formulario
        return redirect(to="listar_notificaciones")
        
    return render(request,'app/notificacion/agregar-notificacion.html',data)

def modificar_notificacion(request,id):
    global notificacion
    notificacions=get_object_or_404(notificacion,id=id)
    
    data={
        'form':NotificacionForm(instance=notificacions)
    }
    if request.method=='POST':
        formulario=NotificacionForm(data=request.POST ,instance=notificacions ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_notificaciones")
        data [ "form"]=formulario
        
    return render(request,"app/notificacion/modificar-notificacion.html",data)
    
def eliminar_notificacion(request,id):
    eliminar=get_object_or_404(notificacion,id=id)
    eliminar.delete()
    return redirect(to="listar_notificaciones")


def listar_notificaciones(request):
    notificaciones=notificacion.objects.all()
    data={
        'notificaciones':notificaciones
    }
    return render (request,'app/notificacion/listar-notificacion.html',data)


def agregar_residente (request):
    data={
        'form':ResidenteForm()
    }
    if request.method=='POST':
        formulario =ResidenteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data[ "mensaje"]="mensaje guardado"
        else:
            data[ "form"]=formulario
        return redirect(to="listar_residentes")
        
    return render(request,'app/residente/agregar-residente.html',data)


def modificar_residente(request,id):
    residentes=get_object_or_404(residente,id=id)
    
    data={
        'form':ResidenteForm(instance=residentes)
    }
    if request.method=='POST':
        formulario=ResidenteForm(data=request.POST ,instance=residentes ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_residentes")
        data [ "form"]=formulario
        
    return render(request,"app/residente/modificar-residente.html",data)

def listar_residentes(request):
    residentes=residente.objects.all()
    data={
        'residentes':residentes
    }
    return render (request,'app/residente/listar-residente.html',data)

def eliminar_residente(request,id):
    eliminar=get_object_or_404(residente,id=id)
    eliminar.delete()
    return redirect(to="listar_residentes")


def home (request):
    return render(request , 'app/home.html')