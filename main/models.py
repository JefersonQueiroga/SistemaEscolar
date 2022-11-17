from secrets import choice
from django.db import models



class Professor(models.Model):
    nome = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome

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

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome + " - " +  self.campus.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    curso  = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Oferta(models.Model):
    periodo = models.CharField(max_length=20)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    capacitade_aluno = models.IntegerField()
    alunos = models.ManyToManyField(Aluno)

    @property
    def disciplina_nome(self):
        return "%s"%(self.disciplina.nome)