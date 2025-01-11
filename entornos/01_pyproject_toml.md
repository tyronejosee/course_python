# **pyproject.toml**

El archivo `pyproject.toml` es un estándar en Python introducido por [PEP 518](https://peps.python.org/pep-0518/). Este archivo sirve como una configuración unificada para proyectos de **Python**, permitiendo especificar dependencias, herramientas de compilación y configuraciones para diversos sistemas en un solo lugar.

## **¿Por qué es importante?**

1. **Estándar moderno**: Se está convirtiendo en el estándar para gestionar la configuración de proyectos de Python, reemplazando archivos como `setup.py`, `requirements.txt`, y `setup.cfg` en muchos casos.
2. **Soporte para múltiples herramientas**: Es compatible con herramientas como:
   - `poetry`: Para gestión de dependencias y empaquetado.
   - `black`: Para configuración de formateadores de código.
   - `mypy`: Para configuraciones de tipado estático.
   - `flit` o `setuptools`: Para empaquetado de proyectos.
3. **Centralización**: Permite centralizar la configuración del proyecto en un único archivo.

## **Ventajas**

- **Universalidad**: Una única configuración para múltiples herramientas.
- **Facilidad de lectura**: Formato TOML (similar a INI) es fácil de leer y escribir.
- **Compatibilidad futura**: Alineado con los estándares modernos de Python.
- **Portabilidad**: Puedes compartir fácilmente la configuración con tu equipo.

### **Estructura de un Archivo**

#### **1. Configuración básica (PEP 518)**

Incluye la configuración para la construcción del proyecto y las dependencias necesarias para este proceso.

Ejemplo:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

- `requires`: Lista de dependencias necesarias para construir el proyecto.
- `build-backend`: Herramienta que se usará para construir el proyecto (por ejemplo, `setuptools`, `flit` o `poetry`).

#### **2. Configuración para `poetry`**

`poetry` es una herramienta popular para gestionar dependencias y empaquetar proyectos de Python.

Ejemplo:

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "Un ejemplo de proyecto con pyproject.toml"
authors = ["Tu Nombre <tu.email@example.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.28.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0"
black = "^23.1"
```

- **Sección `[tool.poetry]`**: Configuración principal del proyecto.

  - `name`: Nombre del proyecto.
  - `version`: Versión del proyecto.
  - `description`: Breve descripción del proyecto.
  - `authors`: Lista de autores.
  - `license`: Tipo de licencia.
  - `readme`: Archivo de documentación.

- **Sección `[tool.poetry.dependencies]`**: Lista de dependencias del proyecto.

  - Especifica las versiones compatibles de las bibliotecas.

- **Sección `[tool.poetry.dev-dependencies]`**: Dependencias para desarrollo, como herramientas de prueba y formateadores.

## **Configuración con Herramientas Externas**

Puedes usar `pyproject.toml` para configurar otras herramientas.

- **Black (formateador de código)**:

```toml
[tool.black]
line-length = 88
target-version = ['py38', 'py39']
skip-string-normalization = true
```

- **Mypy (tipado estático)**:

```toml
[tool.mypy]
strict = true
ignore_missing_imports = true
```

- **Flake8 (linter)**:

```toml
[tool.flake8]
max-line-length = 88
exclude = ["venv", "__pycache__"]
```

---

## **Configuración personalizada**

Puedes definir tus propias configuraciones personalizadas para herramientas o sistemas propios.

```toml
[tool.mytool]
setting1 = "value1"
setting2 = 42
```

---

### **Cómo usar `pyproject.toml` en tu proyecto**

1. **Crear el archivo**:

   - Puedes crearlo manualmente o usar herramientas como `poetry`:
     ```bash
     poetry init
     ```

2. **Instalar dependencias**:

   - Con `poetry`:
     ```bash
     poetry install
     ```

3. **Construir el proyecto**:

   - Si usas `setuptools`:
     ```bash
     python -m build
     ```

4. **Actualizar dependencias**:
   - Con `poetry`:
     ```bash
     poetry update
     ```
