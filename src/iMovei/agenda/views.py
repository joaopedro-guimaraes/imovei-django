from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from iMovei.agenda.models import Visita
from iMovei.agenda.forms import VisitaForm


@login_required
def home(request):
    return render(request, 'agenda/home.html')


@login_required
def read_all(request):
    visitas = Visita.objects.all()

    return render(request, 'agenda/lista_visitas.html', {'visitas': visitas})


@login_required
def create_visita(request):
    form = VisitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agenda:lista_visitas')
    return render(request, 'agenda/cadastro_visita.html', {'form': form})


@login_required
def update_visita(request, id):
    visita = get_object_or_404(Visita, pk=id)
    form = VisitaForm(request.POST or None, instance=visita)
    if form.is_valid():
        form.save()
        return redirect('agenda:lista_visitas')
    return render(request, 'agenda/cadastro_visita.html', {'form': form})


@login_required
def detalhar_visita(request, id):
    visita = get_object_or_404(Visita, pk=id)

    return render(request, 'agenda/detalhamento_visita.html', {'visita': visita})
