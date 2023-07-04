from django.shortcuts import render, get_object_or_404, redirect
from .models import Consumidor
from .forms import ConsumidorForm

def lista_consumidores(request):
    consumidores = Consumidor.objects.all()
    return render(request, 'consumidores/lista_consumidores.html', {'consumidores': consumidores})

def adicionar_consumidor(request):
    if request.method == 'POST':
        form = ConsumidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumidores:lista_consumidores')
    else:
        form = ConsumidorForm()
    return render(request, 'consumidores/adicionar_consumidor.html', {'form': form})

def editar_consumidor(request, pk):
    consumidor = get_object_or_404(Consumidor, pk=pk)
    if request.method == 'POST':
        form = ConsumidorForm(request.POST, instance=consumidor)
        if form.is_valid():
            form.save()
            return redirect('consumidores:lista_consumidores')
    else:
        form = ConsumidorForm(instance=consumidor)
    return render(request, 'consumidores/editar_consumidor.html', {'form': form, 'consumidor': consumidor})

def remover_consumidor(request, pk):
    consumidor = get_object_or_404(Consumidor, pk=pk)
    if request.method == 'POST':
        consumidor.delete()
        return redirect('consumidores:lista_consumidores')
    return render(request, 'consumidores/remover_consumidor.html', {'consumidor': consumidor})

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