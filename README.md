# Preentrega Automation Testing

## Propósito del proyecto

Automatizar pruebas funcionales del sitio web [saucedemo.com](https://www.saucedemo.com/) usando Selenium y pytest. Las pruebas cubren el login, la navegación por el catálogo y la interacción con el carrito de compras.


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
pip install selenium 
pip install pytest 
pip install pytest-html

```

## Ejecución de las pruebas

**Correr todas las pruebas en terminal:**

```bash
python -m pytest test.py -v
```

**Correr una sola prueba en terminal:**

```bash
python -m pytest test.py::test_agregar_productos -v
```

**Generar un reporte HTML en terminal:**

```bash
python -m pytest test.py -v --html=reporte.html
```
