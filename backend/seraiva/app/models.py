from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

class UsuarioCustomizado(AbstractBaseUser,PermissionsMixin):
    nome = models.CharField(max_length=200)
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    
    objects = Gerenciador()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.CharField(max_length=2000)
    foto = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome


class Formato(models.Model):
    CATEGORIAS_FORMATO = (
        ('EBOOK', 'E-book'),
        ('FISICO', 'Físico'),
    )

    nome = models.CharField(max_length=20, choices=CATEGORIAS_FORMATO, primary_key=True)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    ano = models.PositiveIntegerField()
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    qtd_paginas = models.PositiveIntegerField()
    formato = models.ForeignKey('Formato', on_delete=models.CASCADE)
    numero_edicao = models.PositiveIntegerField()
    descricao = models.TextField()
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.PositiveIntegerField()
    estrelas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    foto = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome

STATUS_PAGAMENTO = [
    ("P", "PENDENTE"),
    ("A", "APROVADO"),
    ("R", "RECUSADO"),
    ("C", "CANCELADO"),
]

class Emprestimo(models.Model):
    usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='UsuarioCustomizado', on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO)

    def __str__(self):
        return self.status


class ItemLivro(models.Model):
    livroFK = models.ForeignKey('Livro', on_delete=models.CASCADE)
    emprestimoFK = models.ForeignKey('Emprestimo', on_delete=models.CASCADE)
    qtd_livro = models.IntegerField()

    def __str__(self):
        return f"{self.livroFK} - {self.emprestimoFK}"