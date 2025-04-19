# Wellness Matcher CLI 🌱🧘‍♀️ 

**Wellness Matcher** es una aplicación de línea de comandos (CLI) escrita en Python que simula un sistema de recomendaciones personalizadas de bienestar. A través de un formulario, te genera sugerencias de recursos (rutinas de ejercicio, artículos y planes alimenticios) que se ajustan a tus necesidades. Utiliza clases, persistencia en JSON y lógica de recomendación. Fue pensada como la base para ser escalada a un proyecto en FastAPI.

---

## Tecnologías usadas 💾

| Recurso      | ¿Para qué fue utilizado?        | 
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
│   │   ├── user.py
│   │   └── resource.py
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

---

### 2. Clonar o descargar el repositorio

Si ya tenés Git instalado, podés clonar el repositorio con:

```bash
git clone https://github.com/jossmarsala/wellness-matcher-cli.git
```

Si no usás Git, podés descargar el proyecto como `.zip` desde GitHub haciendo clic en el botón **Code** > **Download ZIP**.

---

### 3. Crear un entorno virtual (recomendado)

Aislá las dependencias del proyecto creando un entorno virtual. Podés hacerlo desde la terminal o usando Visual Studio Code.

#### 👉 Desde la terminal

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

#### 👉 Desde Visual Studio Code

1. Abrí la paleta de comandos (`Ctrl+Shift+P` o `Cmd+Shift+P` en Mac).
2. Buscá `Python: Create Environment` y seguí los pasos para crear y activar el entorno.

---

### 4. Instalar dependencias

Con el entorno activado, instalá las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar la app 🎯

Corré el archivo principal desde la terminal:

```bash
python main.py
```

¡Listo! Ya tenés todo preparado para empezar a usar **Wellness Matcher CLI** ✨

---

## ¿Quién está detrás de este proyecto? 🌷

👩‍💻 Mi nombre es **Josefina Marsala**  
💼 Entusiasta del bienestar digital y el diseño con propósito. Este proyecto forma parte de mi formación en Python, y es la base para una futura API de recomendaciones personalizadas integradas con front-end y bases de datos reales.

  - Github: [@jossmarsala](https://github.com/jossmarsala)  
  - Contacto: marsalahjosefina@gmail.com

> _"Proyecto desarrollado con `python` y mucha intención <3"_ 
