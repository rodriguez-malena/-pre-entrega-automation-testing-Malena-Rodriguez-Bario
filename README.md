# Preentrega Automation Testing

## Propósito del proyecto

Automatizar pruebas funcionales del sitio [saucedemo.com](https://www.saucedemo.com/) usando Selenium y pytest. Las pruebas cubren el login, la navegación por el catálogo y la interacción con el carrito de compras.

### Casos de prueba

**Automatización de login** (`test_login_exitoso`)
1. Navegar a la página de login de saucedemo.com.
2. Ingresar credenciales válidas (usuario: `standard_user`, contraseña: `secret_sauce`).
3. Validar el login exitoso verificando la redirección a la página de inventario.

**Navegación y verificación del catálogo** (`test_navegacion_inventario`, `test_elementos_interfaz`)

4. Verificar que el título de la página de inventario sea correcto ("Swag Labs" y "Products").
5. Comprobar que haya productos visibles en la página (al menos uno).
6. Validar que los elementos importantes de la interfaz estén presentes: menú, filtro de ordenamiento y carrito.

**Interacción con productos** (`test_agregar_productos`)

7. Añadir un producto al carrito haciendo clic en su botón.
8. Verificar que el contador del carrito se incremente correctamente.
9. Navegar al carrito de compras.
10. Comprobar que el producto añadido aparezca correctamente en el carrito.

## Tecnologías utilizadas

- **Python 3**: lenguaje de programación.
- **Selenium WebDriver**: automatiza el navegador.
- **pytest**: framework para escribir y ejecutar las pruebas.
- **pytest-html**: genera reportes HTML con los resultados.
- **Google Chrome**: navegador donde se ejecutan las pruebas.

## Estructura del proyecto

```
├── auxiliar.py   # Funciones reutilizables (login)
├── test.py       # Casos de prueba
└── README.md
```

## Instalación de dependencias

1. Tener instalado [Python 3](https://www.python.org/downloads/) y Google Chrome.
2. Instalar las librerías desde una terminal:

```bash
pip install selenium pytest pytest-html
```

No hace falta descargar ChromeDriver aparte. Selenium (versión 4.6 o superior) lo descarga automáticamente.

## Ejecución de las pruebas

Desde la carpeta del proyecto:

**Correr todas las pruebas:**

```bash
python -m pytest test.py -v
```

**Correr una sola prueba:**

```bash
python -m pytest test.py::test_agregar_productos -v
```

**Generar un reporte HTML:**

```bash
python -m pytest test.py -v --html=reporte.html
```

Al ejecutarlas se abre una ventana de Chrome por cada prueba. Al final, pytest muestra un resumen con las pruebas que pasaron (`PASSED`) y las que fallaron (`FAILED`).
