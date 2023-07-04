from django.urls import path

from . import views

app_name = 'estoque'

urlpatterns = [
    path('estoque/', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('emprestimos/registrados/', views.emprestimos_registrados, name='emprestimos_registrados'),
    path('relatorio_emprestimos/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
    path('gerar_relatorio_pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]
