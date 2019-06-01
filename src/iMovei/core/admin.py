from django.contrib import admin
from iMovei.agenda.models import Visita
from iMovei.clientes.models import Cliente
from iMovei.imoveis.models import Imovel

admin.site.register(Visita)
admin.site.register(Cliente)
admin.site.register(Imovel)
