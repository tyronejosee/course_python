# **YAPF (Yet Another Python Formatter)**

Es una herramienta de formateo de código para Python creada por Google. Su objetivo es reformatear el código de acuerdo con estilos configurables, asegurando un estilo consistente en todo el proyecto. A diferencia de **Black**, que impone un solo estilo, YAPF permite una mayor personalización.

## **Instalación**

Puedes instalar YAPF con `pip`.

```bash
pip install yapf
```

Para verificar la instalación.

```bash
yapf --version
```

## **Uso Básico**

### **Formatear un archivo completo**

```bash
yapf -i script.py
```

- La opción `-i` modifica el archivo original en su lugar.
- Si omites `-i`, mostrará los cambios en la terminal sin modificar el archivo.

### **Formatear múltiples archivos**

```bash
yapf -i script1.py script2.py
```

### **Formatear todo un directorio**

```bash
yapf -ir src/
```

- `-r`: Recorrer recursivamente la carpeta.
- `-i`: Aplicar cambios directamente a los archivos.

## **Configuración**

YAPF permite personalizar las reglas de formateo mediante diferentes archivos de configuración.

- `setup.cfg`
- `pyproject.toml`
- `tox.ini`
- `.style.yapf` (archivo dedicado para YAPF)

### **Ejemplo de `.style.yapf`**

```ini
[style]
based_on_style = pep8
column_limit = 88
indent_width = 4
spaces_before_comment = 2
split_before_logical_operator = true
blank_line_before_nested_class_or_def = true
```

O si prefieres usar `pyproject.toml`:

```toml
[tool.yapf]
based_on_style = "google"
column_limit = 100
indent_width = 4
spaces_before_comment = 2
split_before_logical_operator = true
blank_line_before_nested_class_or_def = true
```

Para aplicar YAPF con la configuración personalizada:

```bash
yapf -i --style .style.yapf script.py
```

## **Estilos Soportados**

YAPF admite varios estilos de formateo predeterminados.

- `pep8` (estándar de la comunidad Python)
- `google` (basado en la guía de estilo de Google)
- `facebook` (basado en la guía de estilo de Facebook)
- `yapf` (estilo original de YAPF)

Ejemplo para usar un estilo específico.

```bash
yapf --style google -i script.py
```

## **Opciones Comunes**

| Opción               | Descripción                                            |
| -------------------- | ------------------------------------------------------ |
| `-i`                 | Modifica el archivo en su lugar.                       |
| `--style <estilo>`   | Especifica un estilo de formateo (pep8, google, etc.). |
| `--diff`             | Muestra los cambios propuestos sin aplicarlos.         |
| `--recursive` o `-r` | Aplica el formateo de forma recursiva en carpetas.     |
| `--in-place`         | Guarda los cambios en el archivo original.             |
| `--parallel`         | Procesa múltiples archivos en paralelo.                |
| `--verbose`          | Muestra detalles del proceso de formateo.              |
| `--dry-run`          | Muestra los cambios sin aplicarlos.                    |

Ejemplo de ejecución con varias opciones.

```bash
yapf --style google --recursive --in-place src/
```

## **Comparación con Otras Herramientas**

| Característica | YAPF                | Black               | Ruff (formateo)    |
| -------------- | ------------------- | ------------------- | ------------------ |
| Flexibilidad   | Alta (configurable) | Baja (opción única) | Moderada           |
| Velocidad      | Media               | Alta                | Muy alta (en Rust) |
| Popularidad    | Media               | Alta                | Creciente          |
| Integración    | Buena               | Excelente           | Buena              |

- **YAPF** permite una configuración flexible, pero es más lento que **Black**.
- **Black** es más estricto, aplicando un solo estilo.
- **Ruff**, aunque principalmente es un linter, también tiene capacidades de formateo.

## **Integración con Editores**

### **VS Code**

Para usar YAPF en **Visual Studio Code**, instala la extensión oficial de Python y configura el formateador:

1. Abre `settings.json` en VS Code.
2. Agrega la configuración:

```json
{
  "python.formatting.provider": "yapf",
  "editor.formatOnSave": true
}
```

### **PyCharm**

1. Ve a **File > Settings > Tools > External Tools**.
2. Agrega una nueva herramienta con:
   - Name: `YAPF`
   - Program: `yapf`
   - Arguments: `-i $FilePath$`
   - Working directory: `$ProjectFileDir$`
3. Guarda y úsalo con **Tools > External Tools > YAPF**.

## **Integración con pre-commit**

Para formatear automáticamente antes de hacer un commit.

Instala `pre-commit`.

```bash
pip install pre-commit
```

Crea un archivo `.pre-commit-config.yaml`.

```yaml
repos:
  - repo: https://github.com/google/yapf
    rev: stable
    hooks:
      - id: yapf
        args: ["--in-place"]
```

Instala el hook.

```bash
pre-commit install
```

## **Integración en CI/CD**

Puedes añadir YAPF a pipelines de integración continua, por ejemplo, en **GitHub Actions**:

```yaml
name: Lint and Format
on: [push, pull_request]
jobs:
  yapf-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install YAPF
        run: pip install yapf

      - name: Run YAPF
        run: yapf --recursive --diff .
```

## **Consejos Prácticos**

- **Usa un archivo de configuración**: Define un estilo personalizado para mantener consistencia en el equipo.
- **Agrega YAPF al pre-commit**: Evita errores de estilo antes de hacer commits.
- **Integra YAPF con Black o Ruff**: YAPF ofrece flexibilidad, pero Black o Ruff pueden ser más rápidos y estrictos.
- **Automatiza el formateo**: Configura `editor.formatOnSave` en tu IDE para formateo automático.
- **Excluye directorios innecesarios**: Usa `--exclude` para omitir archivos generados o de terceros.
