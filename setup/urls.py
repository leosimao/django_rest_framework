from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import (
    AlunoViewSet,
    CursoViewSet,
    ListaMatriculaAluno,
    MatriculaViewSet
)

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Aluno')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno-matricula', ListaMatriculaAluno.as_view())
]
