from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from iMovei.imoveis.models import Imovel
from iMovei.imoveis.forms import ImovelForm


@login_required
def home(request):
    return render(request, 'imoveis/home.html')

@login_required
def read_all(request):
    imoveis = Imovel.objects.all()
    termo_de_busca = ''

    if 'busca' in request.GET:
        termo_de_busca = request.GET['busca']
        imoveis = imoveis.filter(id__icontains=termo_de_busca)
    
    return render(request, 'imoveis/lista_imoveis.html', {'imoveis': imoveis, 'termo_de_busca': termo_de_busca})

@login_required
def create(request):
    form = ImovelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('imoveis:lista_imoveis')
    return render(request, 'imoveis/cadastro.html', {'form': form})

@login_required
def update(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    form = ImovelForm(request.POST or None, instance=imovel)
    if form.is_valid():
        form.save()
        return redirect('imoveis:lista_imoveis')
    return render(request, 'imoveis/cadastro.html', {'form': form})

@login_required
def delete(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    form = ImovelForm(request.POST or None, instance=imovel)
    if request.method == 'POST':
        imovel.delete()
        return redirect('imoveis:lista_imoveis')
    return render(request, 'imoveis/confirma_exclusao.html', {'form': form, 'imovel': imovel})
