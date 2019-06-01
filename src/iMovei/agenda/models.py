from django.db import models

from iMovei.clientes.models import Cliente
from iMovei.imoveis.models import Imovel


class Visita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    data_visita = models.DateField(auto_now=False, auto_now_add=False)
    hora_visita = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return 'Visita {0}: agendada para o dia {1}.'.format(self.id, self.data_visita)
