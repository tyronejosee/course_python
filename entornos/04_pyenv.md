# **pyenv**

Es una herramienta para gestionar múltiples versiones de **Python** en tu sistema. Es especialmente útil si necesitas trabajar con diferentes versiones en varios proyectos, ya que te permite instalar, cambiar y administrar versiones fácilmente.

### **Características principales**

- **Instalación de múltiples versiones de Python**:

  - Soporta versiones estándar de Python, como Python 2.x, 3.x.
  - Compatible con implementaciones como PyPy y Anaconda.

- **Cambiar entre versiones global o localmente**:

  - Configura una versión global (predeterminada) o una específica para un proyecto.

- **Aislamiento de versiones**:
  - Cada proyecto puede usar una versión de Python diferente sin conflictos.

---

### **Instalación de `pyenv`**

1. **Instalar `pyenv` en sistemas basados en Unix**:

   - En macOS o Linux, usa el siguiente comando:

     ```bash
     curl https://pyenv.run | bash
     ```

   - Asegúrate de añadir estas líneas a tu archivo de configuración de shell (`~/.bashrc`, `~/.zshrc`, etc.):
     ```bash
     export PATH="$HOME/.pyenv/bin:$PATH"
     eval "$(pyenv init --path)"
     eval "$(pyenv virtualenv-init -)"
     ```

2. **En Windows**:

   - Usa [pyenv-win](https://github.com/pyenv-win/pyenv-win) para instalar y gestionar `pyenv` en sistemas Windows.

3. **Instalar dependencias necesarias** (para compilación):
   - Antes de instalar versiones de Python con `pyenv`, asegúrate de que las dependencias están instaladas. Por ejemplo, en Ubuntu:
     ```bash
     sudo apt update
     sudo apt install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
       libncurses5-dev libncursesw5-dev xz-utils tk-dev \
       libffi-dev liblzma-dev python3-openssl git
     ```

---

## **Comandos**

- **1. Instalar una nueva versión de Python**

```bash
pyenv install 3.11.6
```

- Muestra todas las versiones disponibles:
  ```bash
  pyenv install --list
  ```

#### **2. Usar una versión globalmente**

```bash
pyenv global 3.11.6
```

- Esto establece la versión predeterminada de Python en tu sistema.

#### **3. Usar una versión localmente (proyecto específico)**

```bash
pyenv local 3.9.13
```

- Esto crea un archivo `.python-version` en el directorio actual para especificar la versión de Python.

#### **4. Ver la versión actual de Python**

```bash
pyenv version
```

#### **5. Mostrar todas las versiones instaladas**

```bash
pyenv versions
```

#### **6. Desinstalar una versión de Python**

```bash
pyenv uninstall 3.10.12
```

---

### **Uso avanzado con `pyenv`**

#### **1. Aislar entornos virtuales con `pyenv-virtualenv`**

`pyenv` puede integrarse con `pyenv-virtualenv` para gestionar entornos virtuales.

- Instalar `pyenv-virtualenv`:

  ```bash
  git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
  ```

- Crear un entorno virtual:

  ```bash
  pyenv virtualenv 3.11.6 myenv
  ```

- Activar un entorno virtual:

  ```bash
  pyenv activate myenv
  ```

- Desactivar el entorno virtual:
  ```bash
  pyenv deactivate
  ```

#### **2. Solucionar conflictos de PATH**

Cuando instalas `pyenv`, puede interferir con la instalación de Python de tu sistema. Asegúrate de que `pyenv` esté primero en tu variable `PATH`:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
```

---

### **Beneficios de usar `pyenv`**

1. **Simplifica el desarrollo con múltiples proyectos**:

   - Asegura que cada proyecto tenga su propia versión de Python.
   - Compatible con herramientas como `pipenv`, `poetry`, y `venv`.

2. **Control total sobre las versiones de Python**:

   - Instalar y cambiar entre versiones de Python es rápido y fácil.

3. **Portabilidad**:
   - Facilita compartir proyectos con configuraciones específicas mediante el archivo `.python-version`.

---

### **Ejemplo práctico con `pyenv`**

#### Escenario: Tienes dos proyectos con diferentes versiones de Python.

1. Instalas las versiones necesarias:

   ```bash
   pyenv install 3.10.6
   pyenv install 3.9.13
   ```

2. Configuras una versión global para tu sistema:

   ```bash
   pyenv global 3.10.6
   ```

3. Configuras una versión local para un proyecto específico:

   - Dentro del directorio del proyecto:
     ```bash
     cd proyecto-antiguo
     pyenv local 3.9.13
     ```

4. Verificas las versiones:

   ```bash
   pyenv version
   ```

   Salida:

   ```
   3.9.13 (set by /ruta/proyecto-antiguo/.python-version)
   ```

---

Si necesitas ayuda con instalación o uso específico de `pyenv`, ¡avísame! 😊
