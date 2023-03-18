from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
#from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from trabajo.models import Estudiante, Profesor, Curso
from trabajo.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario


def index(request):
    return render(
        request=request,
        template_name='trabajo/index.html',
    )


# 

def listar_estudiantes(request):
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='trabajo/lista_estudiantes.html',
        context=contexto,
    )

def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='trabajo/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='trabajo/lista_cursos.html',
        context=contexto,
    )


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    contexto = {
        'curso': curso
    }
    return render(
        request=request,
        template_name='trabajo/detalle_curso.html',
        context=contexto,
    )


# def crear_curso_version_1(request):
#     """No la estamos usando"""
#     if request.method == "POST":
#         data = request.POST
#         curso = Curso(nombre=data['nombre'], comision=data['comision'])
#         curso.save()
#         url_exitosa = reverse('listar_cursos')
#         return redirect(url_exitosa)
#     else:  # GET
#         return render(
#             request=request,
#             template_name='estudiantes/formulario_curso_a_mano.html',
#         )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'], descripcion=data['descripcion'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='trabajo/formulario_curso.html',
        context={'formulario': formulario},
    )


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.descripcion = data['descripcion']
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
            'descripcion': curso.descripcion,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='trabajo/formulario_curso.html',
        context={'formulario': formulario, 'curso': curso, 'es_update': True},
    )


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(nombre__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='trabajo/lista_cursos.html',
            context=contexto,
        )
    

#### Profesores

def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'])
            profesor.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    return render(
        request=request,
        template_name='trabajo/formulario_profesor.html',
        context={'formulario': formulario},
    )

def buscar_profesores(request):
    if request.method == "POST":
        data = request.POST
        profesores = Profesor.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'profesores': profesores
        }
        return render(
            request=request,
            template_name='trabajo/lista_profesores.html',
            context=contexto,
        )

def ver_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    contexto = {
        'profesor': profesor
    }
    return render(
        request=request,
        template_name='trabajo/detalle_profesor.html',
        context=contexto,
    )


def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
 
        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
    else:  # GET
       inicial = {
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
       }
       formulario = ProfesorFormulario(initial=inicial)
    return render(
       request=request,
       template_name='trabajo/formulario_profesor.html',
       context={'formulario': formulario, 'profesor': profesor, 'es_update': True},
    )


def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        profesor.delete()
        url_exitosa = reverse('listar_profesores')
        return redirect(url_exitosa)
    


#####  Estudiantes

def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'])
            estudiante.save()
            url_exitosa = reverse('listar_estudiantes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    return render(
        request=request,
        template_name='trabajo/formulario_estudiantes.html',
        context={'formulario': formulario},
    )

def buscar_estudiante(request):
    if request.method == "POST":
        data = request.POST
        estudiantes = Estudiante.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(nombre__exact=data['busqueda'])
        )
        contexto = {
            'estudiantes': estudiantes
        }
        return render(
            request=request,
            template_name='trabajo/lista_estudiantes.html',
            context=contexto,
        )
    


def ver_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    contexto = {
        'estudiante': estudiante
    }
    return render(
        request=request,
        template_name='trabajo/detalle_estudiantes.html',
        context=contexto,
    )

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.save()
            url_exitosa = reverse('listar_estudiantes')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
        }
        formulario = EstudianteFormulario(initial=inicial)
    return render(
        request=request,
        template_name='trabajo/formulario_estudiantes.html',
        context={'formulario': formulario, 'estudiante': estudiante, 'es_update': True},
    )


def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        estudiante.delete()
        url_exitosa = reverse('listar_estudiantes')
        return redirect(url_exitosa)

