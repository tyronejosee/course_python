# **virtualenv**

Es una herramienta popular para crear y gestionar entornos virtuales en **Python**. Los entornos virtuales permiten que cada proyecto tenga sus propias dependencias, aisladas de las del sistema global, lo que evita conflictos entre paquetes.

## **Ventajas**

- **Aislamiento de Proyectos**: Cada proyecto tiene sus propias dependencias, evitando conflictos.
- **Compatibilidad de Versiones**: Permite trabajar con diferentes versiones de Python o dependencias específicas para diferentes proyectos.
- **Evitar Dependencias Globales**: Instalar paquetes globalmente puede causar conflictos entre proyectos; `virtualenv` resuelve esto creando entornos separados.

## **Comandos**

### Instalación

```bash
pip install virtualenv
```

### Crear un Entorno Virtual

```bash
virtualenv <nombre_entorno>
```

### Activar el Entorno Virtual

```bash
# Windows
<nombre_entorno>\Scripts\activate

# macOS/Linux
source <nombre_entorno>/bin/activate
```

Cuando el entorno esté activado, verás el nombre del entorno al principio de la línea de comandos, indicando que cualquier paquete que instales o ejecutes será aislado.

### Desactivar el Entorno Virtual

```bash
deactivate
```

### Instalar Paquetes en el Entorno Virtual

```bash
pip install <nombre_paquete>
```

### Eliminar un Entorno Virtual

Para eliminar un entorno virtual, solo tienes que borrar la carpeta que contiene el entorno

```bash
rm -rf <nombre_entorno>
```

### **Usar `requirements.txt` con `virtualenv`**

- Con el entorno activado, ejecuta

  ```bash
  pip freeze > requirements.txt
  ```

- Instalar esas dependencias con:

  ```bash
  pip install -r requirements.txt
  ```
