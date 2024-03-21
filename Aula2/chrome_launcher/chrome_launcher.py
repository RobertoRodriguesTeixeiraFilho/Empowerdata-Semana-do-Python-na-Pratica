'''
    Contém uma função que abrirá o google chrome de forma automática no Windows
'''
from pyautogui import press, write

def open_chrome():
    '''
    Função que abrirá o Menu Iniciar do Windows, digitará Chrome e pressionará enter
    '''
    press("win")
    write("chrome")
    press("enter")
