from django import forms

from blog.models import Autor, Categoria, Post


class AutorModelForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellido", "email", "bio"]


class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "resumen", "contenido", "autor", "categoria", "publicado"]


class BusquedaForm(forms.Form):
    query = forms.CharField(
        label="Buscar posts",
        max_length=200,
    )
