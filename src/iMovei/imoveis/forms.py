from django.forms import ModelForm
from .models import Imovel


class ImovelForm(ModelForm):
  class Meta:
    model = Imovel
    fields = [
      'operacao',
      'finalidade',
      'valor_condominio',
      'valor_iptu',
      'garagem',
      'tipo_garagem',
      'dormitorios',
      'sendo_suite',
      'banheiros',
      'face',
      'area_terreno',
      'area_construida',
      'frente',
      'fundo',
      'esquerda',
      'direita',
      'cep',
      'rua',
      'numero',
      'bairro',
      'cidade',
      'estado',
      'complemento'
    ]
