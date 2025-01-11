# **Pipenv**

Es una herramienta para gestionar dependencias y entornos virtuales en proyectos de Python. Combina las funcionalidades de `pip` (gestión de paquetes) y `virtualenv` (entornos virtuales) para ofrecer una solución integrada.

## **Ventajas**

- **Entornos Virtuales Automatizados:** Crea y gestiona entornos virtuales automáticamente.
- **Gestión de Dependencias:** Usa un archivo `Pipfile` para declarar dependencias y un `Pipfile.lock` para bloquear versiones específicas.
- **Seguridad:** Verifica vulnerabilidades de seguridad en las dependencias.
- **Compatibilidad:** Compatible con Python 2 y Python 3.

## **Archivos Clave**

### **`Pipfile`**

- Reemplaza el `requirements.txt`.
- Define las dependencias del proyecto, con separaciones para producción y desarrollo.

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true

[packages]
django = ">=4.0"

[dev-packages]
pytest = "*"
```

### **`Pipfile.lock`**

- Archivo generado automáticamente.
- Bloquea las versiones específicas de los paquetes instalados para garantizar reproducibilidad.

---

## **Comandos**

### Instala Pipenv

```bash
pip install pipenv
```

> Puedes necesitar permisos de administrador o usar `--user` para instalarlo localmente.

### Instala dependencias

```bash
pipenv install <paquete>
```

### Instala dependencias de desarrollo

```bash
pipenv install <paquete> --dev
```

> Especifica versiones compatibles, por ejemplo, `Django>=4.0`.

### Activa el entorno virtual

```bash
pipenv shell
```

### Desactiva el entorno virtual

```bash
exit
```

### Si ya tienes un proyecto con un `Pipfile`, instala dependencias

```bash
pipenv install
```

### Elimina un paquete del entorno y del `Pipfile`

```bash
pipenv uninstall <paquete>
```

### Actualiza todas las dependencias bloqueadas en `Pipfile.lock`

```bash
pipenv update
```

### Lista las dependencias instaladas

```bash
pipenv graph
```

### Especifica una versión de Python para el entorno

```bash
pipenv --python 3.9
```

> Pipenv descargará la versión si no está instalada (si usas `pyenv`).

### Busca vulnerabilidades en las dependencias

```bash
pipenv check
```

### Genera un `Pipfile` desde un archivo `requirements.txt`

```bash
pipenv install -r requirements.txt
```
