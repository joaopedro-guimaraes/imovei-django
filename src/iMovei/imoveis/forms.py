from django import forms
from .models import Imovel


class ImovelForm(forms.ModelForm):
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

        widgets = { 
            "cep":forms.TextInput(attrs={
                'name':'cep',
                'type':'text',
                'placeholder':'XXXXX-XXX',
                'id':'cep',
                'onblur':'pesquisacep(this.value);'}),
            "rua":forms.TextInput(attrs={
                'name':'rua',
                'type':'text',
                'id':'rua'}),
            "bairro":forms.TextInput(attrs={
                'name':'bairro',
                'type':'text',
                'id':'bairro'}),
            "cidade":forms.TextInput(attrs={
                'name':'cidade',
                'type':'text',
                'id':'cidade'}),
            "estado":forms.TextInput(attrs={
                'name':'estado',
                'type':'text',
                'id':'uf'}),
        }  
