from django.forms import ModelForm
from iMovei.clientes.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'pessoa',
            'nome',
            'cpf',
            'idade',
            'sexo',
            'email',
            'telefone',
            'telefone2'
        ]
