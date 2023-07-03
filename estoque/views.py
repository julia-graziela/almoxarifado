from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

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

