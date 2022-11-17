from django.contrib import admin
from main.models import *
# Register your models here.


class OfertaAdmin(admin.ModelAdmin):
    list_display = ['disciplina_nome','curso','periodo']
    
    def disciplina_nome(self, obj):
        return obj.disciplina.nome

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome','carga_horaria']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome','nome_campus']
    
    def nome_campus(self, obj):
        return obj.campus.nome


admin.site.register(Aluno)
admin.site.register(Campus)
admin.site.register(Professor)
admin.site.register(Oferta,OfertaAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)