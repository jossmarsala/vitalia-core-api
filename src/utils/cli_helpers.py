# Funciones auxiliares para el CLI

import os
from rich import print as rich_print

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux o Mac
        os.system('clear')

def show_menu():
    rich_print("[bold yellow]Hi!")
