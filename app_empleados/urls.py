from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_empleados, name='ver_empleados'),
    path('agregar/', views.agregar_empleados, name='agregar_empleados'),
    path('editar/<int:id>/', views.editar_empleados, name='editar_empleados'),
    path('borrar/<int:id>/', views.borrar_empleados, name='borrar_empleados'),
]