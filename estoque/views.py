from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Emprestimo
from .forms import ProdutoForm, EmprestimoForm
from django.db.models import Count
from django.db.models.functions import TruncMonth

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form})

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('estoque:lista_produtos')
    return render(request, 'estoque/remover_produto.html', {'produto': produto})

def emprestimos(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:emprestimos')
    else:
        form = EmprestimoForm()
    emprestimos = Emprestimo.objects.all()
    return render(request, 'estoque/emprestimos.html', {'form': form, 'emprestimos': emprestimos})

def emprestimos_registrados(request):
    emprestimos = Emprestimo.objects.all()
    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimo_id')
        quantidade_devolvida = int(request.POST.get('quantidade_devolvida'))
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

        if quantidade_devolvida >= emprestimo.quantidade:
            # Remove o registro do empréstimo se a quantidade devolvida for igual ou superior à quantidade original
            emprestimo.delete()
        else:
            # Atualiza apenas a quantidade devolvida no registro do empréstimo
            emprestimo.quantidade -= quantidade_devolvida
            emprestimo.save()

    return render(request, 'estoque/emprestimos_registrados.html', {'emprestimos': emprestimos})

def relatorio_emprestimos(request):
        emprestimos_por_mes_ano = Emprestimo.objects.annotate(
            mes_ano=TruncMonth('data_emprestimo')
        ).values('mes_ano').annotate(total_emprestimos=Count('id')).order_by('mes_ano')
    
        return render(request, 'estoque/relatorio_emprestimos.html', {'emprestimos_por_mes_ano': emprestimos_por_mes_ano})
