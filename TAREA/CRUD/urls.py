
from django.urls import path, include
from .import views 

urlpatterns = [
    path('index/', views.index,name="index"),
    path('inicio/', views.inicio,name="inicio"),
    path('inicioP/', views.inicioP,name="inicioP"),
    path('lista/', views.lista, name="lista"),
    path('listaP/', views.listaP, name="listaP"),
    path('ActualizarCliente/<int:id>', views.ActualizarC, name="ActualizarCliente"),
    path('ActualizarPedido/<int:id>', views.ActualizarP, name="ActualizarPedido"),
    path('eliminarCliente/<int:id>', views.eliminarCliente, name="eliminarCliente"),
    path('eliminarP/<int:id>', views.eliminarP, name="eliminarP")

]