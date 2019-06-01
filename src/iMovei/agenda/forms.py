from django.forms import ModelForm
from iMovei.agenda.models import Visita


class VisitaForm(ModelForm):
    class Meta:
        model = Visita
        fields = [
            'cliente',
            'imovel',
            'data_visita',
            'hora_visita'
        ]
