from django.urls import path

from . import views

app_name = 'consumidores'

urlpatterns = [
    path('consumidores/', views.lista_consumidores, name='lista_consumidores'),
    path('consumidores/adicionar/', views.adicionar_consumidor, name='adicionar_consumidor'),
    path('consumidores/editar/<int:pk>/', views.editar_consumidor, name='editar_consumidor'),
    path('consumidores/remover/<int:pk>/', views.remover_consumidor, name='remover_consumidor'),
]