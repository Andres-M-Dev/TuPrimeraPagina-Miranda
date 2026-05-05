# DevBlog — Proyecto Django

Blog desarrollado con Django usando el patrón **MVT** (Modelo - Vista - Template).


---

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPO>
cd blogproject

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instalar Django
pip install django

# 4. Aplicar migraciones
python manage.py migrate

# 5. (Opcional) Crear superusuario para el panel admin
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000**

---

## Orden para probar las funcionalidades

### 1. Registrar un Autor
- Ir a **Autores → + Nuevo Autor** en la barra de navegación
- URL: `/autores/nuevo/`
- Completar: nombre, apellido, email y (opcionalmente) biografía
- Guardar → redirige al listado de autores

### 2. Crear una Categoría
- Ir a **Categorías → + Nueva Categoría** en la barra de navegación
- URL: `/categorias/nueva/`
- Completar: nombre y descripción
- Guardar → redirige al listado de categorías

### 3. Crear un Post
- Ir a **+ Nuevo Post** en la barra de navegación
- URL: `/posts/nuevo/`
- Completar todos los campos (requiere al menos 1 autor y 1 categoría ya creados)
- Guardar → redirige al listado de posts

### 4. Ver Posts
- Ir a **Posts** en la navegación → URL: `/posts/`
- Hacer clic en el título de cualquier post para ver su detalle
- Desde el detalle se puede editar o eliminar el post

### 5. Editar / Eliminar
- Cada listado (Posts, Autores, Categorías) tiene botones de Editar y Eliminar
- Eliminar pide confirmación con un `confirm()` nativo del navegador

### 6. Buscar Posts
- Ir a **🔍 Buscar** en la navegación → URL: `/buscar/`
- Ingresar una palabra del título o contenido de algún post
- El formulario usa método GET (aparece en la URL)

### 7. Panel de administración (opcional)
- URL: `/admin/`
- Requiere haber creado un superusuario (`python manage.py createsuperuser`)

---

## Estructura del proyecto

```
blogproject/
│
├── blogproject/              # Configuración del proyecto Django
│   ├── settings.py           # Configuración general
│   ├── urls.py               # URLs raíz → include("blog.urls")
│   └── wsgi.py
│
├── blog/                     # Aplicación principal
│   ├── migrations/           # Migraciones generadas automáticamente
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html               ← Plantilla BASE (herencia)
│   │       ├── inicio.html             ← extends base.html
│   │       ├── lista_posts.html        ← extends base.html
│   │       ├── detalle_post.html       ← extends base.html
│   │       ├── formulario_post.html    ← extends base.html
│   │       ├── lista_autores.html      ← extends base.html
│   │       ├── formulario_autor.html   ← extends base.html
│   │       ├── lista_categorias.html   ← extends base.html
│   │       ├── formulario_categoria.html ← extends base.html
│   │       └── buscar.html             ← extends base.html
│   │
│   ├── models.py       # Modelos: Autor, Categoria, Post
│   ├── views.py        # Vistas (funciones)
│   ├── forms.py        # ModelForms para los 3 modelos + BusquedaForm
│   ├── urls.py         # URLs de la app blog
│   └── admin.py        # Registro en el panel admin
│
├── db.sqlite3          # Base de datos SQLite
└── manage.py
```

---

## Requisitos cumplidos

| Requisito | Implementación | Estado |
|-----------|----------------|--------|
| Herencia de HTML | `base.html` con `{% block contenido %}`, todas las templates usan `{% extends "blog/base.html" %}` | ✅ |
| 3 clases en models | `Autor`, `Categoria`, `Post` en `blog/models.py` | ✅ |
| Formulario para insertar datos (por cada modelo) | `formulario_autor.html`, `formulario_categoria.html`, `formulario_post.html` — cada uno con su `ModelForm` | ✅ |
| Formulario de búsqueda en la BD | `buscar.html` con `BusquedaForm` (GET), busca en `titulo` y `contenido` de Post | ✅ |
| Patrón MVT | Models → `models.py`, Views → `views.py`, Templates → `templates/blog/` | ✅ |
| README con orden de prueba | Este archivo | ✅ |

---

## Modelos (`blog/models.py`)

### Autor
| Campo | Tipo |
|-------|------|
| nombre | CharField(100) |
| apellido | CharField(100) |
| email | EmailField (único) |
| bio | TextField (opcional) |
| fecha_creacion | DateTimeField (auto) |

### Categoria
| Campo | Tipo |
|-------|------|
| nombre | CharField(80) |
| descripcion | TextField (opcional) |

### Post
| Campo | Tipo |
|-------|------|
| titulo | CharField(200) |
| contenido | TextField |
| resumen | CharField(300, opcional) |
| autor | ForeignKey → Autor |
| categoria | ForeignKey → Categoria |
| fecha_publicacion | DateTimeField (auto) |
| fecha_actualizacion | DateTimeField (auto) |
| publicado | BooleanField |
