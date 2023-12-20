from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    ListaMatriculaAlunoSerializer,
    MatriculaSerializer
)

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculaAluno(generics.ListAPIView):
    queryset = Matricula.objects.values(
        'curso__curso_matricula',
        'periodo'
    )
    serializer_class = ListaMatriculaAlunoSerializer(queryset)