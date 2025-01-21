# **Black**

Es un formateador de código para **Python** que sigue el principio de "configuración mínima" y aplica reglas de estilo de código consistentes basadas en **PEP 8**, asegurando código limpio y legible. Es ampliamente utilizado para mantener la uniformidad en proyectos colaborativos.

## **Instalación**

Puedes instalar **Black** usando `pip`.

```bash
pip install black
```

Si usas **Poetry** o **pipenv**, puedes instalarlo como dependencia de desarrollo.

```bash
poetry add black --dev
pipenv install black --dev
```

Para verificar si está instalado correctamente.

```bash
black --version
```

## **Uso Básico**

Formatear un archivo de Python específico.

```bash
black archivo.py
```

Formatear todos los archivos dentro de un directorio.

```bash
black nombre_del_directorio/
```

Ejemplo con múltiples archivos.

```bash
black script1.py script2.py
```

Realizar una prueba sin modificar los archivos.

```bash
black --check archivo.py
```

Obtener estadísticas de los cambios realizados.

```bash
black --diff archivo.py
```

Formatear archivos con un nivel de detalle alto.

```bash
black -v archivo.py
```

Formatear con confirmación interactiva.

```bash
black --preview archivo.py
```

## **Configuración**

Puedes personalizar el comportamiento de Black creando un archivo de configuración como **`pyproject.toml`** en la raíz de tu proyecto.

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | build
  | dist
)/
'''
```

Luego, puedes ejecutar Black normalmente y tomará los ajustes desde el archivo de configuración.

```bash
black .
```

## **Opciones Comunes**

| Opción                 | Descripción                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `-l` o `--line-length` | Especifica la longitud máxima de línea (por defecto 88).       |
| `--check`              | Verifica si los archivos cumplen con el formato sin modificar. |
| `--diff`               | Muestra las diferencias sin aplicar cambios.                   |
| `--color`              | Muestra la salida con colores.                                 |
| `--verbose`            | Muestra más información del proceso.                           |
| `--quiet`              | No muestra mensajes de salida.                                 |
| `--fast`               | Formateo más rápido pero menos seguro.                         |
| `--safe`               | Asegura un formateo seguro (modo predeterminado).              |
| `--target-version`     | Define la versión de Python objetivo (`py37`, `py38`, etc.).   |
| `--exclude`            | Excluye ciertos archivos o directorios del formateo.           |

Ejemplo.

```bash
black --line-length 100 --exclude "migrations" .
```

## **Integración con Editores**

### **VS Code**

Para configurar Black como el formateador por defecto en **VS Code**, instala la extensión **Python** y luego agrega lo siguiente a tu `settings.json`.

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

También puedes ejecutar manualmente el formateo con `Ctrl + Shift + P` y escribiendo `Format Document`.

---

### **PyCharm**

1. Ve a **File > Settings > Tools > External Tools**.
2. Añade un nuevo "External Tool" con la configuración:
   - Name: `Black`
   - Program: `black`
   - Arguments: `$FilePath$`
   - Working directory: `$ProjectFileDir$`
3. Guarda y luego puedes ejecutar Black desde el menú de herramientas.

## **Integración con pre-commit**

Puedes automatizar Black usando **pre-commit**, asegurando que el código se formatee antes de cada commit:

Instala `pre-commit`.

```bash
pip install pre-commit
```

Crea un archivo `.pre-commit-config.yaml` en la raíz del proyecto.

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0 # Sustituir por la última versión
    hooks:
      - id: black
        args: ["--line-length=88"]
```

Instala el hook de pre-commit.

```bash
pre-commit install
```

Ahora, cada vez que intentes hacer `git commit`, Black verificará el código y lo formateará si es necesario.

## **Comparación con Otros Formateadores**

| Herramienta  | Filosofía            | Configuración | Popularidad | Integración |
| ------------ | -------------------- | ------------- | ----------- | ----------- |
| **Black**    | Opinión única        | Mínima        | Alta        | Alta        |
| **Autopep8** | Respeta PEP 8        | Configurable  | Media       | Media       |
| **YAPF**     | Estilo flexible      | Alta          | Media       | Media       |
| **isort**    | Ordena importaciones | Mínima        | Alta        | Alta        |

## **Desventajas**

- Impone un estilo rígido sin flexibilidad.
- Puede ser lento en archivos muy grandes.
- No permite ciertas personalizaciones avanzadas como otros formateadores.
- Puede entrar en conflicto con otros linters si no se configura correctamente.

## **Consejos Prácticos**

- Usa Black junto con herramientas como `flake8` o `pylint` para verificar el estilo.
- Configura Black en tu CI/CD para asegurarte de que todos sigan el mismo formato.
- Aprovecha la opción `--check` en tus revisiones de código sin modificar el original.
- Personaliza la longitud de línea para adaptarla a tu equipo.
