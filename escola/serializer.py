from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        
class ListaMatriculaAlunoSerializer(serializers.Serializer):
    curso = serializers.SerializerMethodField()
    periodo = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'curso',
            'periodo',
        )

    def get_curso(self, instance):
        return instance['curso__curso_matricula']

    def get_periodo(self, instance):
        return instance['periodo']