from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from iMovei.clientes.models import Cliente
from iMovei.clientes.forms import ClienteForm


@login_required
def home(request):
    return render(request, 'clientes/home.html')


@login_required
def read_all(request):
    clientes = Cliente.objects.all()
    termo_de_busca = ''

    if 'busca' in request.GET:
        termo_de_busca = request.GET['busca']
        clientes = clientes.filter(nome__icontains=termo_de_busca)

    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes, 'termo_de_busca': termo_de_busca})


@login_required
def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:lista_clientes')
    return render(request, 'clientes/cadastro.html', {'form': form})


@login_required
def update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('clientes:lista_clientes')
    return render(request, 'clientes/cadastro.html', {'form': form})


@login_required
def delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:lista_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'form': form, 'cliente': cliente})
