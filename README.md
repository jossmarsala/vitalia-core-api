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
.gitignore
main.py                        
readme.md
requirements.txt
src/
├── config/
│   └── constants.py           # rutas de los JSON, texto base, tags por default
│
├── controllers/
│   └── match_controller.py    # lógica de matching
│
├── data/
│   ├── db.py                  # leer/escribir usuarios y recursos
│   └── users.json
│   └── resources.json
│
├── utils/
│   └── cli_helpers.py         # estilos para questionary/rich
│
├── models/
│   └── user.py
│   └── resource.py
│
├── app.py                     # tu aplicación principal (funciones, flujo)
└── __init__.py
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
