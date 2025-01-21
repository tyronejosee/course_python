# **Ruff**

Es una herramienta rápida y eficiente para analizar y formatear código **Python**. Combina funcionalidades de varios linters y formateadores en una sola herramienta, como **Flake8, Pyflakes, Pycodestyle, Mypy, isort**, entre otros. Ruff es escrito en **Rust**, lo que lo hace extremadamente rápido en comparación con otras herramientas de análisis estático en **Python**.

## **Instalación**

Puedes instalar Ruff usando `pip`.

```bash
pip install ruff
```

Si usas **Poetry** o **pipenv**, puedes instalarlo como dependencia de desarrollo.

```bash
poetry add ruff --dev
pipenv install ruff --dev
```

Para verificar si está instalado correctamente.

```bash
ruff --version
```

## **Uso Básico**

### **Análisis de código**

Para analizar errores de estilo y convenciones en un archivo.

```bash
ruff archivo.py
```

Para analizar todos los archivos dentro de un proyecto.

```bash
ruff .
```

Ejemplo con múltiples archivos.

```bash
ruff script1.py script2.py
```

### **Corrección Automática de Errores**

Ruff puede corregir automáticamente algunos errores detectados.

```bash
ruff --fix archivo.py
```

### **Ordenar importaciones (equivalente a isort)**

```bash
ruff --fix --select I archivo.py
```

### **Ver solo problemas sin modificar archivos**

```bash
ruff --check archivo.py
```

### **Mostrar las reglas activas y su código**

```bash
ruff --explain E501
```

## **Configuración**

Puedes personalizar Ruff creando un archivo de configuración en **`pyproject.toml`**, **`ruff.toml`** o **`.ruffrc`**, en la raíz del proyecto.

Ejemplo básico de `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py39"
fixable = ["ALL"]
select = ["E", "F", "I", "UP", "D"]
ignore = ["E203", "E501"]
exclude = ["migrations", "tests"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

Luego, ejecuta Ruff y aplicará la configuración personalizada.

```bash
ruff .
```

## **Opciones Comunes**

| Opción         | Descripción                                           |
| -------------- | ----------------------------------------------------- |
| `--fix`        | Corrige automáticamente los problemas detectados.     |
| `--check`      | Solo analiza sin realizar cambios.                    |
| `--select`     | Especifica qué reglas aplicar (ej. "E", "F", "I").    |
| `--ignore`     | Excluye reglas específicas.                           |
| `--exclude`    | Omite archivos y directorios.                         |
| `--config`     | Especifica un archivo de configuración personalizado. |
| `--diff`       | Muestra los cambios propuestos sin aplicarlos.        |
| `--statistics` | Muestra estadísticas de los errores encontrados.      |

Ejemplo de ejecución con opciones combinadas.

```bash
ruff --fix --select E,F,I --exclude "migrations,tests" .
```

## **Integración con Editores**

### **VS Code**

Para configurar Ruff en **VS Code**, instala la extensión oficial `Ruff` desde la tienda de extensiones y agrega en `settings.json`.

```json
{
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "editor.formatOnSave": true,
  "ruff.args": ["--fix"]
}
```

Puedes ejecutar Ruff manualmente con `Ctrl + Shift + P` → `Run Ruff`.

### **PyCharm**

1. Ve a **File > Settings > Tools > External Tools**.
2. Añade un nuevo "External Tool" con la configuración:
   - Name: `Ruff`
   - Program: `ruff`
   - Arguments: `--fix $FilePath$`
   - Working directory: `$ProjectFileDir$`
3. Guarda y ejecuta Ruff desde el menú de herramientas.

## **Integración con pre-commit**

Para automatizar Ruff y ejecutarlo antes de hacer un commit, puedes configurar **pre-commit**.

Instala `pre-commit`.

```bash
pip install pre-commit
```

Crea un archivo `.pre-commit-config.yaml` en la raíz del proyecto.

```yaml
repos:
   - repo: https://github.com/charliermarsh/ruff-pre-commit
      rev: v0.4.1 # Sustituir por la última versión
      hooks:
      - id: ruff
         args: ["--fix"]
```

Instala el hook de pre-commit.

```bash
pre-commit install
```

Ahora, Ruff se ejecutará automáticamente antes de cada commit.

## **Comparación con Otras Herramientas**

| Herramienta | Funcionalidades       | Velocidad | Popularidad | Facilidad de uso |
| ----------- | --------------------- | --------- | ----------- | ---------------- |
| **Ruff**    | Linter + Formateador  | Muy alta  | Creciente   | Alta             |
| **Black**   | Solo formateador      | Alta      | Alta        | Alta             |
| **Flake8**  | Solo linter           | Media     | Alta        | Media            |
| **isort**   | Ordenar importaciones | Alta      | Alta        | Alta             |
| **Mypy**    | Tipado estático       | Media     | Alta        | Media            |

## **Desventajas**

- Aún está en desarrollo activo, por lo que algunas características pueden cambiar.
- Puede ser más estricto que otras herramientas en ciertas reglas de estilo.
- No ofrece la misma profundidad de análisis de tipos que **Mypy**.

## **Consejos Prácticos**

- Configura Ruff junto con Black para formateo y análisis de errores completo.
- Úsalo en entornos CI/CD para mantener estándares de calidad en tu código.
- Excluye directorios innecesarios para mejorar la velocidad de análisis.
- Usa la opción `--fix` para corregir problemas rápidamente.
