from django.urls import path
from iMovei.agenda.views import home, create_visita, read_all, update_visita, detalhar_visita


app_name = 'agenda'

urlpatterns = [
    path('', home, name='home_agenda'),
    path('lista/', read_all, name="lista_visitas"),
    path('cadastro_visita/', create_visita, name="cadastro_visita"),
    path('atualizar/<int:id>/', update_visita, name="atualizar_visita"),
    path('detalhamento/<int:id>/', detalhar_visita, name="detalhamento_visita"),
    #path('excluir/<int:id>/', delete, name="excluir_clientes"),
]
