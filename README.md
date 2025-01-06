# GreenWolf E-commerce Web App

## Descripción
GreenWolf es una aplicación web de comercio electrónico diseñada específicamente para la impresión 3D. La plataforma permite a los usuarios cargar, personalizar, y visualizar modelos 3D en tiempo real. Adicionalmente, incluye funcionalidades de catálogo de productos, carrito de compras, y procesamiento de pedidos.

## Funcionalidades principales

### Para Usuarios
- **Registro e inicio de sesión:** Permite crear una cuenta o autenticarse en el sistema.
- **Cargar y personalizar modelos 3D:** Los usuarios pueden subir archivos (STL/OBJ) y personalizar modelos ajustando tamaño, calidad y materiales.
- **Visualización 3D:** Visualización en tiempo real de los modelos cargados o personalizados mediante un visor integrado.
- **Carrito de compras:** Agregar, eliminar y gestionar productos antes de confirmar el pago.
- **Notificaciones:** Recibir actualizaciones sobre el estado de pedidos y otras acciones.

### Para Administradores
- **Gestión de usuarios:** Administrar las cuentas de los usuarios.
- **Gestión de catálogo:** Añadir, editar y eliminar productos del catálogo.
- **Gestión de inventario y precios:** Controlar la disponibilidad de materiales y precios de productos.
- **Gestión de pedidos:** Procesar y actualizar estados de pedidos.

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Ve al directorio del proyecto:
   ```bash
   cd webapp
   ```
3. Instala las dependencias necesarias usando `pip`:
   ```bash
   pip install -r requirements.txt
   ```
4. Realiza las migraciones de base de datos:
   ```bash
   python manage.py migrate
   ```
5. Ejecuta el servidor local:
   ```bash
   python manage.py runserver
   ```
6. Accede a la aplicación desde tu navegador en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
