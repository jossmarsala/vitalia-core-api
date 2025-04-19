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

## 🗂️ Estructura del proyecto

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

## ¿Quién está detrás de este proyecto? 🌷

👩‍💻 Mi nombre es **Josefina Marsala**  
💼 Entusiasta del bienestar digital y el diseño con propósito. Este proyecto forma parte de mi formación en Python, y es la base para una futura API de recomendaciones personalizadas integradas con front-end y bases de datos reales.

  - Github: [@jossmarsala](https://github.com/jossmarsala)  
  - Contacto: marsalahjosefina@gmail.com

> _"Proyecto desarrollado con `python` y mucha intención <3"_ 
