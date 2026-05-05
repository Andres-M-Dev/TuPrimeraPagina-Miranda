## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone <https://github.com/Andres-M-Dev/TuPrimeraPagina-Miranda.git >
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

