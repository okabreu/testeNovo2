from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','nome','email','endereco','cpf']
        many = True

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        many = True

class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formato
        fields = '__all__'
        many = True

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        many = True

class LivroSerializer(serializers.ModelSerializer):
    categoriaFK = FormatoSerializer(read_only=True)
    class Meta:
        model = Livro
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        many = True

class ItemLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLivro
        fields = '__all__'
        many = True