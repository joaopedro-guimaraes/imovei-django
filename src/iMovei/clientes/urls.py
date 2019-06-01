from django.urls import path
from iMovei.clientes.views import home, read_all, create, update, delete


app_name = 'clientes'

urlpatterns = [
    path('', home, name='home_clientes'),
    path('lista/', read_all, name="lista_clientes"),
    path('cadastro/', create, name="cadastro_clientes"),
    path('atualizar/<int:id>/', update, name="atualizar_clientes"),
    path('excluir/<int:id>/', delete, name="excluir_clientes"),
]
