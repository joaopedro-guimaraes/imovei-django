from django.urls import path
from iMovei.imoveis.views import home, read_all, create, update, delete


app_name = 'imoveis'

urlpatterns = [
    path('', home, name='home_imoveis'),
    path('lista/', read_all, name="lista_imoveis"),
    path('cadastro/', create, name="cadastro_imoveis"),
    path('atualizar/<int:id>/', update, name="atualizar_imoveis"),
    path('excluir/<int:id>/', delete, name="excluir_imoveis"),
]
