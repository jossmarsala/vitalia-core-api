# Wellness Matcher CLI 🌱🧘‍♀️ 

**Wellness Matcher** es una aplicación de línea de comandos (CLI) escrita en Python que simula un sistema de recomendaciones personalizadas de bienestar. A través de un formulario, te genera sugerencias de recursos (rutinas, artículos y planes alimenticios) que se ajustan a tus necesidades. Utiliza clases, persistencia en JSON y lógica de recomendación. Fue pensada como la base para ser escalada a un proyecto en FastAPI.

---

## Tecnologías usadas 💾

| Recurso      | ¿Para qué fue utilizado?        | 
|:--------------:|:------------------|
| **Python 3.13+** | Lenguaje base del proyecto | 
| `questionary` | Mejoró la experiencia de usuario al completar el formulario |
| `rich` | Embelleció el formato y la apariencia del código |
| `json (built-in)`	| Para almacenar y persistir los datos de usuarios, preferencias y recursos sin una base de datos externa |
<br />

---

## 🗂️ Estructura del proyecto

Diseñé así la estructura con el objetivo mantener mi código limpio, organizado y fácil de escalar:

``` 
wellness-matcher/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml          ← opcional, para herramientas modernas
├── main.py                 ← punto de entrada
├── src/
│   ├── __init__.py
│   ├── app.py              ← función run_app
│
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py     ← configuración general (como dotenv o constantes)
│
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── match_controller.py
│
│   ├── data/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── resources.json
│   │   └── users.json
│
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── resource.py
│
│   ├── services/           ← lógica intermedia entre controladores y datos
│   │   ├── __init__.py
│   │   └── recommender.py  ← ejemplo de motor de recomendaciones
│
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── cli_helpers.py
│   │   └── decorators.py   ← decoradores útiles, si los usás

``` 

>_Estructura inspirada en las recomendaciones de [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/structure/), una guía creada por usuarios de la comunidad Python 🧭✨._
<br />

---

## ¿Quién está detrás de este proyecto? 🌷

👩‍💻 Mi nombre es **Josefina Marsala**  
💼 Entusiasta del bienestar digital y el diseño con propósito. Este proyecto forma parte de mi formación en Python, y es la base para una futura API de recomendaciones personalizadas integradas con front-end y bases de datos reales.

  - Github: [@jossmarsala](https://github.com/jossmarsala)  
  - Contacto: marsalahjosefina@gmail.com

> _"Proyecto desarrollado con `python` y mucha intención <3"_ 
