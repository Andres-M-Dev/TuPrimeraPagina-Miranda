from django.contrib import admin

from blog.models import Autor, Categoria, Post


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "email", "fecha_creacion"]
    search_fields = ["nombre", "apellido", "email"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "categoria", "publicado", "fecha_publicacion"]
    list_filter = ["publicado", "categoria"]
    search_fields = ["titulo", "contenido"]
