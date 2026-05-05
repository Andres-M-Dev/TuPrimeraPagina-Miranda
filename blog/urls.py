from django.urls import path

from blog.views import (
    inicio,
    lista_posts, detalle_post, crear_post, editar_post, eliminar_post,
    lista_autores, crear_autor, editar_autor, eliminar_autor,
    lista_categorias, crear_categoria, editar_categoria, eliminar_categoria,
    buscar_posts,
)

urlpatterns = [
    path("", inicio, name="inicio"),

    # Posts
    path("posts/", lista_posts, name="lista_posts"),
    path("posts/<int:id>/", detalle_post, name="detalle_post"),
    path("posts/nuevo/", crear_post, name="crear_post"),
    path("posts/editar/<int:id>/", editar_post, name="editar_post"),
    path("posts/eliminar/<int:id>/", eliminar_post, name="eliminar_post"),

    # Autores
    path("autores/", lista_autores, name="lista_autores"),
    path("autores/nuevo/", crear_autor, name="crear_autor"),
    path("autores/editar/<int:id>/", editar_autor, name="editar_autor"),
    path("autores/eliminar/<int:id>/", eliminar_autor, name="eliminar_autor"),

    # Categorías
    path("categorias/", lista_categorias, name="lista_categorias"),
    path("categorias/nueva/", crear_categoria, name="crear_categoria"),
    path("categorias/editar/<int:id>/", editar_categoria, name="editar_categoria"),
    path("categorias/eliminar/<int:id>/", eliminar_categoria, name="eliminar_categoria"),

    # Búsqueda
    path("buscar/", buscar_posts, name="buscar_posts"),
]
