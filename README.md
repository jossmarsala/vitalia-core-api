<h1 style="display: flex;">
    <img
    src="https://raw.githubusercontent.com/jossmarsala/jossmarsala/main/butterfly.gif"
    width="40px"
    style="margin-top: 10px;
    margin-left: 20px;"
  />
  ‎ Vitalia Core API
</h1>

**Vitalia Core** es una API que funciona como backend de [Vitalia Selfcare](https://www.vitalia-selfcare.vercel.app), una plataforma de bienestar que recomienda recursos personalizados (rutinas, artículos, planes alimenticios) basados en las preferencias del usuario. Esta API contiene un CRUD completo: Gestiona usuarios, recursos y sus puntajes de recomendación, utilizando Firebase Firestore.


---

## Tecnologías usadas 💾

| Recurso      | ¿Para qué se usó?        | 
|:--------------:|:------------------|
| **Python 3.13+** | Lenguaje base del proyecto | 
| `FastAPI` | Para construir la API y ejecutar las operaciones del CRUD |
| `uvicorn`	| Funciona como servidor para la API |
| `Firebase` | Sistema para almacenar y persistir los datos de usuarios, preferencias y recursos |

<br />

---

## Estructura del proyecto 🗂️

La estructura del proyecto fue pensada así para mantener el código limpio, organizado y fácil de escalar:

``` 
vitalia-core-api/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml          
├── main.py
├── src/
│   ├── __init__.py
│   ├── app.py              
│
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user_controller.py
│   │   ├── resource_controller.py
│   │   └── score_controller.py
│
│   ├── database/
│   │   └── database_connection.py       
│
│   ├── exceptions/
│   │   ├── __init__.py
│   │   ├── app_exceptions.py
│   │   ├── client_exception.py
│   │   ├── base_http_exceptions.py
│   │   └── server_exceptions.py
│
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base_repository.py
│   │   ├── resource_repository.py
│   │   ├── score_repository.py
│   │   └── user_repository.py
│
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── score_routes.py
│   │   │   ├── resource_routes.py
│   │   │   ├── user_routes.py
│   │   │   └── dependencies.py
│
│   ├── services/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── score_service.py
│   │   │   ├── resource_service.py
│   │   │   └── user_service.py
│
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── paginated_schemas.py
│   │   ├── resource_schemas.py
│   │   ├── score_schemas.py
│   │   └── user_schemas.py

``` 
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

Ya tenés todo listo para empezar a usar Vitalia Core API.

<br />

---

## ¿Quién está detrás de este proyecto? 🌷

👩‍💻 Mi nombre es **Josefina Marsala**  
💼 Soy entusiasta del bienestar digital y el diseño con propósito.

  - Github: [@jossmarsala](https://github.com/jossmarsala)  
  - Contacto: marsalahjosefina@gmail.com

---

## Licencia 📜

Este proyecto está bajo la licencia MIT. Ver [LICENSE](./LICENSE) para más info.
<br />

---

> _"Proyecto desarrollado con `python` y mucha intención <3"_ 
