from django.db import models


class Imovel(models.Model):
  operacao = models.CharField(
    max_length=1,
    choices=(
      ('V', 'Venda'),
      ('L', 'Locação'),
    ),
    default='V'
  )
  finalidade = models.CharField(
    max_length=1,
    choices=(
      ('R', 'Residencial'),
      ('C', 'Comercial'),
    ),
    default='R'
  )
  valor_condominio = models.DecimalField(max_digits=9, decimal_places=2)
  valor_iptu = models.DecimalField(max_digits=9, decimal_places=2)
  garagem = models.PositiveIntegerField()
  tipo_garagem = models.CharField(
    max_length=1,
    choices=(
      ('C', 'Coberta'),
      ('D', 'Descoberta'),
      ('P', 'Parcial'),
    ),
    default='C'
  )
  dormitorios = models.PositiveIntegerField()
  sendo_suite = models.PositiveIntegerField()
  banheiros = models.PositiveIntegerField()
  face = models.CharField(
    max_length=3,
    choices=(
      ('SOM', 'Sombra'),
      ('SOL', 'Sol'),
    ),
    default='SOM'
  )
  area_terreno = models.DecimalField(max_digits=9, decimal_places=2)
  area_construida = models.DecimalField(max_digits=9, decimal_places=2)
  frente = models.DecimalField(max_digits=9, decimal_places=2)
  fundo = models.DecimalField(max_digits=9, decimal_places=2)
  esquerda = models.DecimalField(max_digits=9, decimal_places=2)
  direita = models.DecimalField(max_digits=9, decimal_places=2)

  # ENDEREÇO
  cep = models.CharField(max_length=10, blank=False, default='')
  rua = models.CharField(max_length=50, blank=False, default='')
  numero = models.PositiveIntegerField(blank=False, default=0)
  bairro = models.CharField(max_length=50, blank=False, default='')
  cidade = models.CharField(max_length=30, blank=False, default='')
  estado = models.CharField(max_length=20, blank=False, default='')
  complemento = models.TextField(max_length=150, blank=True)

  def __str__(self):
    return 'Código do imóvel: {}'.format(str(self.id))
