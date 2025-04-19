# Lógica para leer y sobrescribir archivos

import json

def read_json(path: str) -> list[dict]:
    try: 
        with open(path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        write_json(path, [])
        return []
 
def write_json(path: str, content: list) -> None:
    with open (path, "w") as file:
        json.dump(content, file, indent = 4, ensure_ascii = False)