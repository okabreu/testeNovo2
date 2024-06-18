from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# class CustomModelViewSet(ModelViewSet):
#     def create(self, request, *args, **kwargs):
#         mySerializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))

class UsuarioView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UsuarioCustomizado.objects.get(pk=user.id)
        return queryset

class AutorView(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class FormatoView(ModelViewSet):
    queryset = Formato.objects.all()
    serializer_class = FormatoSerializer
    permission_classes = (IsAuthenticated,)

class GeneroView(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class LivroView(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    
class ItemLivroView(ModelViewSet):
    queryset = ItemLivro.objects.all()
    serializer_class = ItemLivroSerializer