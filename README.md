<h1 style="display: flex;">
    <img
    src="https://raw.githubusercontent.com/jossmarsala/jossmarsala/main/butterfly.gif"
    width="40px"
    style="margin-top: 10px;
    margin-left: 20px;"
  />
  ‎ Vitalia Core: API para <a href="https://github.com/gracimarch/Vitalia" target"_blank">Vitalia Selfcare</a>
</h1>

**Wellness Matcher** es una aplicación de línea de comandos (CLI) hecha en Python que simula un sistema de recomendaciones personalizadas de bienestar. A través de un formulario, te genera sugerencias de recursos (rutinas de ejercicio, artículos y planes alimenticios) que se ajustan a tus necesidades. Utiliza clases, persistencia en JSON y lógica de recomendación. Fue pensada como la base para ser escalada a un proyecto en FastAPI y ser implementada en el proyecto [Vitalia Selfcare](https://www.vitalia-selfcare.vercel.app).

---

## Tecnologías usadas 💾

| Recurso      | ¿Para qué se usó?        | 
|:--------------:|:------------------|
| **Python 3.13+** | Lenguaje base del proyecto | 
| `questionary` | Mejorar la UX al completar el formulario |
| `rich` | Embellecer el formato y la apariencia del código |
| `json (built-in)`	| Para almacenar y persistir los datos de usuarios, preferencias y recursos sin una base de datos externa |
<br />

---

## Estructura del proyecto 🗂️

Diseñé así la estructura con el objetivo mantener mi código limpio, organizado y fácil de escalar:

``` 
wellness-matcher/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml          
├── main.py
├── output_json/
│   ├── users.json
│   ├── resources.json
├── src/
│   ├── __init__.py
│   ├── app.py              
│
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py     
│
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user_controller.py
│   │   └── menu_controller.py
│
│   ├── data/
│   │   ├── __init__.py
│   │   ├── resources.json
│   │   └── db.py
│
│   ├── models/
│   │   ├── __init__.py
│   │   ├── temp_user.py
│   │   ├── abstract_user.py
│   │   └── user.py
│
│   ├── services/           
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── matcher.py  
│
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── cli_helpers.py
│   │   ├── app_helpers.py
│   │   └── file_helpers.py 

``` 

>_Estructura inspirada en las recomendaciones de [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/structure/), una guía creada por usuarios de la comunidad._
<br />

---

## Cómo ejecutar el proyecto en tu computadora 🧑‍💻

### 1. Requisitos previos

Asegurate de tener **Python 3.13+** instalado en tu sistema. Podés verificar la versión instalada ejecutando:

```bash
python --version
```

Si no lo tenés instalado, podés descargar la última versión desde la [web oficial de Python](https://www.python.org/downloads/).

<br />

### 2. Clonar o descargar el repositorio

Si ya tenés Git instalado, podés clonar el repositorio con:

```bash
git clone https://github.com/jossmarsala/wellness-matcher-cli.git
```

Si no usás Git, podés descargar el proyecto como `.zip` desde GitHub haciendo clic en el botón **Code** > **Download ZIP**.

<br />

### 3. Crear un entorno virtual

Te recomiendo aislar las dependencias del proyecto creando un entorno virtual. Podés hacerlo desde la terminal o usando VSCode.

#### Desde la terminal

1. Abrí la terminal en la carpeta del proyecto.
2. Ejecutá:

   ```bash
   python -m venv venv
   ```

3. Activá el entorno:

   - En **Linux/MacOS**:

     ```bash
     source venv/bin/activate
     ```

   - En **Windows**:

     ```bash
     venv\Scripts\activate
     ```

#### Desde Visual Studio Code

1. Abrí la paleta de comandos (`Ctrl+Shift+P` o `Cmd+Shift+P` en Mac).
2. Buscá `Python: Create Environment` y seguí los pasos para crear y activar el entorno.

<br />

### 4. Instalar dependencias

Con el entorno activado, instalá las dependencias necesarias con:

```bash
pip install -r requirements.txt
```
<br />

### 5. Ejecutar la app 

Corré el archivo principal desde la terminal:

```bash
python main.py
```

Ya tenés todo listo para empezar a usar Wellness Matcher.

<br />

---

## Modelo de datos ✨
Creé un modelo de usuario ```UserModel``` que contiene los datos básicos de los usuarios, como nombre, contraseña y preferencias.

Por motivos de testing, implementé la clase ```TempUser```, que hereda de ```UserModel```, para de facilitar la prueba de nuevas funcionalidades sin necesidad de crear o modificar usuarios reales. Esta clase genera usuarios temporales con datos automáticos y no persiste en archivos, lo que es muy útil para pruebas rápidas. 

Para utilizarla, podés llamar a la siguiente función:
```bash
from src.utils.app_helpers import test_temp_user
test_temp_user()
```

<br />

---

## ¿Quién está detrás de este proyecto? 🌷

👩‍💻 Mi nombre es **Josefina Marsala**  
💼 Entusiasta del bienestar digital y el diseño con propósito. Este proyecto forma parte de mi formación en Python, y es la base para una futura API de recomendaciones personalizadas integradas con front-end y bases de datos reales.

  - Github: [@jossmarsala](https://github.com/jossmarsala)  
  - Contacto: marsalahjosefina@gmail.com

---

## Licencia 📜

Este proyecto está bajo la licencia MIT. Ver [LICENSE](./LICENSE) para más info.
<br />

---

> _"Proyecto desarrollado con `python` y mucha intención <3"_ 
