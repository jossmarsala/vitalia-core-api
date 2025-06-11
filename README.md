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

Este proyecto usa **Poetry** para la gestión de dependencias. Si no lo tenés instalado, podés hacerlo con:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Luego, instalá las dependencias del proyecto con:

```bash
poetry install
```

Si no usas Poetry, podés simplemente instalar las dependencias haciendo 
```bash
-r requirements.txt
```

<br />

### 5. Configurar variables de entorno

El proyecto utiliza un archivo `.env` para definir variables de configuración.

1. Copiá el archivo de ejemplo:

   ```bash
   cp .env.example .env
   ```

2. Abrí `.env` y completá los valores según tu entorno.

<br />

### 6. Agregar credenciales de Firebase

Para que la API funcione correctamente, necesitás un archivo de credenciales de Firebase:

1. Creá un proyecto en [Firebase Console](https://console.firebase.google.com/).
2. Activá **Firestore** y **Authentication**.
3. Generá una clave privada JSON desde:
   `Configuración del proyecto > Cuentas de servicio > Generar nueva clave privada`.
4. Guardala como `src/database/firebase_credentials.json`.

<br />

### 7. Iniciar la API

Ya con todo listo, ejecutá el servidor de desarrollo:

```bash
poetry run uvicorn src.main:app --reload --port 8008
```

> Podés cambiar el puerto si lo definiste distinto en el `.env`.

<br />

### 8. Acceder a la documentación interactiva

Una vez levantada la API, accedé a la documentación automática:

* Swagger UI: [http://localhost:8008/docs](http://localhost:8008/docs)


<br />

---


## 🧠 Lógica de recomendación

Cuando se crea un nuevo usuario, automáticamente se generan puntajes que relacionan sus preferencias con los recursos disponibles. Esto se logra mediante coincidencias entre los campos del usuario y los campos de cada recurso.

Se seleccionan los **4 recursos más relevantes** para:

* Artículos (`articulos`)
* Rutinas (`rutinas`)
* Planes alimenticios (`planes_alimenticios`)

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
