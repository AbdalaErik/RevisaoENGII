from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.

class ProdutoInLine(admin.TabularInline):
    model = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    inlines = [ProdutoInLine]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "fabricante", "preco", "categoria"]
    search_fields = ["nome"]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)