from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuariocustomizado',UsuarioView)
router.register(r'autor',AutorView)
router.register(r'formato',FormatoView)
router.register(r'genero',GeneroView)
router.register(r'livro',LivroView)
router.register(r'emprestimo',EmprestimoView)
router.register(r'itemLivro',ItemLivroView)

urlpatterns = router.urls