from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from blog.models import Autor, Categoria, Post
from blog.forms import AutorModelForm, CategoriaModelForm, PostModelForm, BusquedaForm


# ── Inicio ───────────────────────────────────────────────────────────────────
def inicio(request):
    posts_recientes = Post.objects.filter(publicado=True)[:6]
    contexto = {
        "posts": posts_recientes,
        "total_posts": Post.objects.filter(publicado=True).count(),
        "total_autores": Autor.objects.count(),
        "total_categorias": Categoria.objects.count(),
    }
    return render(request, "blog/inicio.html", contexto)


# ── Posts ─────────────────────────────────────────────────────────────────────
def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, "blog/lista_posts.html", {"posts": posts})


def detalle_post(request, id):
    post = get_object_or_404(Post, id=id, publicado=True)
    return render(request, "blog/detalle_post.html", {"post": post})


def crear_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            messages.success(request, "Post creado exitosamente.")
            return redirect("lista_posts")
        else:
            print("Error al crear el post:", form.errors)
    # GET
    form = PostModelForm()
    return render(request, "blog/formulario_post.html", {"form": form})


def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado exitosamente.")
            return redirect("lista_posts")
    form = PostModelForm(instance=post)
    return render(request, "blog/formulario_post.html", {"form": form, "editando": True})


def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, f'Post "{post.titulo}" eliminado.')
    return redirect("lista_posts")


# ── Autores ───────────────────────────────────────────────────────────────────
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, "blog/lista_autores.html", {"autores": autores})


def crear_autor(request):
    if request.method == "POST":
        form = AutorModelForm(request.POST)
        if form.is_valid():
            Autor.objects.create(**form.cleaned_data)
            messages.success(request, "Autor registrado exitosamente.")
            return redirect("lista_autores")
        else:
            print("Error al crear el autor:", form.errors)
    # GET
    form = AutorModelForm()
    return render(request, "blog/formulario_autor.html", {"form": form})


def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == "POST":
        form = AutorModelForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor actualizado exitosamente.")
            return redirect("lista_autores")
    form = AutorModelForm(instance=autor)
    return render(request, "blog/formulario_autor.html", {"form": form, "editando": True})


def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    messages.success(request, f'Autor "{autor.nombre} {autor.apellido}" eliminado.')
    return redirect("lista_autores")


# ── Categorías ────────────────────────────────────────────────────────────────
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "blog/lista_categorias.html", {"categorias": categorias})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaModelForm(request.POST)
        if form.is_valid():
            Categoria.objects.create(**form.cleaned_data)
            messages.success(request, "Categoría creada exitosamente.")
            return redirect("lista_categorias")
        else:
            print("Error al crear la categoría:", form.errors)
    # GET
    form = CategoriaModelForm()
    return render(request, "blog/formulario_categoria.html", {"form": form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        form = CategoriaModelForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect("lista_categorias")
    form = CategoriaModelForm(instance=categoria)
    return render(request, "blog/formulario_categoria.html", {"form": form, "editando": True})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, f'Categoría "{categoria.nombre}" eliminada.')
    return redirect("lista_categorias")


# ── Búsqueda ──────────────────────────────────────────────────────────────────
def buscar_posts(request):
    form = BusquedaForm(request.GET or None)
    resultados = []
    query = ""

    if form.is_valid():
        query = form.cleaned_data["query"]
        resultados = Post.objects.filter(publicado=True).filter(
            titulo__icontains=query
        ) | Post.objects.filter(publicado=True).filter(
            contenido__icontains=query
        )
        resultados = resultados.distinct()

    return render(request, "blog/buscar.html", {
        "form": form,
        "resultados": resultados,
        "query": query,
    })
