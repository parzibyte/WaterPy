import os
import webbrowser


def obtener_lista_de_imagenes_en_directorio(directorio):
    imagenes = []
    for fichero_o_directorio in os.listdir(directorio):
        ruta_absoluta = os.path.join(directorio, fichero_o_directorio)
        if os.path.isfile(ruta_absoluta):
            if es_extension_valida(obtener_extension(ruta_absoluta)):
                imagenes.append(ruta_absoluta)
    return imagenes

def es_extension_valida(extension):
    return extension.lower() in [".jpg", ".png"]

def obtener_extension(archivo):
    archivo, extension = os.path.splitext(archivo)
    return extension

def ver_sitio_web_programador():
    webbrowser.open('https://github.com/parzibyte')

def ver_repositorio():
    webbrowser.open('https://github.com/parzibyte')