from django.db import models


class Cliente(models.Model):
  pessoa = models.CharField(
    max_length=1,
    choices=(
      ('F', 'Física'),
      ('J', 'Jurídica'),
    ),
    default='F'
  )
  nome = models.CharField(max_length=50, blank=False, default='')
  cpf = models.CharField(max_length=14, blank=False, default='')
  idade = models.PositiveIntegerField()
  sexo = models.CharField(
    max_length=1,
    choices=(
      ('M', 'Masculino'),
      ('F', 'Feminino'),
      ('X', 'Não informado'),
    ),
    default='X'
  )
  email = models.CharField(max_length=50, blank=True)
  telefone = models.CharField(max_length=25, blank=True)
  telefone2 = models.CharField(max_length=25, blank=True)

  def __str__(self):
    return self.nome
