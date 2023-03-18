"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trabajo.views import( index, crear_curso, buscar_cursos, ver_curso, editar_curso, eliminar_curso, listar_cursos,
    crear_profesor, buscar_profesores, ver_profesor, editar_profesor, eliminar_profesor, listar_profesores,
    crear_estudiante, buscar_estudiante, ver_estudiante, editar_estudiante, eliminar_estudiante, listar_estudiantes, )
urlpatterns = [
    path('',index,name="index"),
    path('admin/', admin.site.urls),
     path('crear-curso/', crear_curso, name="crear_curso"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),


    # URLS de profesores (basadas den views funcionales)
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('buscar-profesores/', buscar_profesores, name="buscar_profesores"),
    path('profesores/<int:id>/', ver_profesor, name="ver_profesor"),
    path('editar-profesor/<int:id>/', editar_profesor, name="editar_profesor"),
    path('eliminar-profesor/<int:id>/', eliminar_profesor, name="eliminar_profesor"),    
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('profesor/<int:id>/', ver_profesor, name="ver_profesor"),

# URLS de estudiantes (basadas den views funcionales)
    path('estudiantes/', listar_estudiantes, name="listar_estudiantes"),
    path('buscar-estudiantes/', buscar_estudiante, name="buscar_estudiante"),
    path('estudiantes/<int:id>/', ver_estudiante, name="ver_estudiante"),
    path('editar-estudiante/<int:id>/', editar_estudiante, name="editar_estudiante"),
    path('eliminar-estudiante/<int:id>/', eliminar_estudiante, name="eliminar_estudiante"),    
    path('crear-estudiante/', crear_estudiante, name="crear_estudiante"),
    path('estudiantes/', ver_estudiante, name="ver_estudiantes"),

]
