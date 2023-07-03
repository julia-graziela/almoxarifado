from django.urls import path

from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
]
