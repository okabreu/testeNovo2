from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    model=UsuarioCustomizado
    list_display = ['nome','email',]
    list_display_links = ['nome','email',]
    fieldsets = (
        (None,{'fields': ('email','password','nome')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome','email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,UsuarioAdmin)

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome','biografia','foto',]
    list_display_links = ['nome','biografia',] 
    search_fields = ['nome',]
    list_per_page = 10

admin.site.register(Autor, AutorAdmin)


class FormatoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome'] 
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(Formato, FormatoAdmin)


class AdminGenero(admin.ModelAdmin):
    list_display = ['nome',]
    list_display_links = ['nome',]
    search_fields = ['nome',]
    list_per_page = 10

admin.site.register(Genero, AdminGenero)


class AdminLivro(admin.ModelAdmin):
    list_display = ('id', 'nome','genero','estrelas','autor',)
    list_display_links = ('nome','genero','autor',)
    search_fields = ('nome', 'genero',)
    list_per_page = 20

admin.site.register(Livro, AdminLivro)


class AdminEmprestimo(admin.ModelAdmin):
    list_display = ('usuarioFK','data_emprestimo','status',)
    list_display_links = ('usuarioFK','data_emprestimo','status',)
    search_fields = ('usuarioFK',)
    list_per_page = 10

admin.site.register(Emprestimo, AdminEmprestimo)


class AdminItem(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(ItemLivro, AdminItem)