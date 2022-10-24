from pyexpat import model
from secrets import choice
from django.db import models

CLASSES_CHOICES = [
        ('TÉCNICO EM INFORMÁTICA', 'TÉCNICO EM INFORMÁTICA'),
        ('TÉCNICO EM ALIMENTOS', 'TÉCNICO EM ALIMENTOS'),
        ('TÉCNICO EM APICULTURA', 'TÉCNICO EM APICULTURA'),
        ('QUÍMICA', 'QUÍMICA'),
        ('ADS', 'ADS'),
    ]

class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome


class Campus(models.Model):
    nome = models.CharField(max_length=150)
    nome_cidade = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    disciplinas = models.ManyToManyField(Disciplina)
    curso = models.CharField(max_length=150,choices=CLASSES_CHOICES)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

