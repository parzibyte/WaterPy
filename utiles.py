import os
import constantes


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


def crear_directorio_si_no_existe(directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio)

def crear_directorio_de_salida(ruta):
    ruta_verdadera = os.path.join(ruta, constantes.NOMBRE_CARPETA_SALIDA)
    crear_directorio_si_no_existe(ruta_verdadera)
    return ruta_verdadera