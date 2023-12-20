from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    list_per_page = 20
    
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao_curso', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', 'nivel')
    list_per_page = 10
    
class MatriculAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')
    
admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculAdmin)