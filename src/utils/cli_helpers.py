# Funciones auxiliares para el CLI

import os

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux o Mac
        os.system('clear')