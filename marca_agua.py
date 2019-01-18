"""
    Gran nota:
    Este es un archivo histórico que utilizaba antes de crear
    waterpy con una interfaz gráfica

    ========================================================================================
    
    Nadie debería usarlo y solamente está aquí para el recuerdo, no forma parte del proyecto
    
    ========================================================================================
    Las "ventajas" que tiene este es que redimensiona la imagen, pero
    siempre la pone en la esquina inferior derecha y no agrega transparencia;
    además de que algunos cálculos están mal

    Su forma de llamarlo era:
    python marca_agua.py ruta/a/carpeta/con/imagenes ruta/a/marca_de_agua.png
    


"""
from os import listdir, getcwd
from os.path import isfile, join
from PIL import Image
import sys
import os

OPACIDAD = 50 # Desde 0 hasta 255
RELACION = 50 # Desde 1 hasta 100
argumentos = sys.argv[1:]
ruta_ubicacion_imagen = ""
if len(argumentos) > 0:
    ruta_ubicacion_imagen = argumentos[0]
else:
    ruta_ubicacion_imagen = input("Ruta de la imagen a la que pondremos la marca de agua: ")


if os.path.isdir(ruta_ubicacion_imagen):
    imagenes = [f for f in listdir(ruta_ubicacion_imagen) if isfile(join(ruta_ubicacion_imagen, f))]
else:
    imagenes = [ruta_ubicacion_imagen]
ruta_marca_de_agua = ""
if len(argumentos) > 1:
    ruta_marca_de_agua = argumentos[1]
else:
    ruta_marca_de_agua = input("Ruta de la imagen que tiene la marca de agua");

marca_de_agua = Image.open(ruta_marca_de_agua)

ruta_guardado = join(ruta_ubicacion_imagen, "marcadas")
if not os.path.isdir(ruta_guardado):
    os.mkdir(ruta_guardado)
for ruta_imagen in imagenes:
    ruta_absoluta_imagen_original = join(ruta_ubicacion_imagen, ruta_imagen)
   
    print("Agregando marca de agua a", ruta_imagen)
    imagen = Image.open(ruta_absoluta_imagen_original)
    print("Cambiando el tamaño de imagen...")
    largo_original, alto_original = imagen.size
    # Sacar el % de la imagen
    ratio_largo = (largo_original / 100) * RELACION
    ratio_alto = (alto_original / 100) * RELACION

    largo_watermark, alto_watermark = marca_de_agua.size
    nuevo_largo, nuevo_alto = 0, 0
    if largo_watermark > ratio_largo:
        print("Largo mayor")
        nuevo_largo = ratio_largo
        relacion = (nuevo_largo * 100) / largo_watermark
        nuevo_alto = (relacion / alto_watermark) * 100
    elif alto_watermark > ratio_alto:
        print("Alto mayor")
        nuevo_alto = ratio_alto
        relacion = (nuevo_alto * 100) / alto_watermark
        nuevo_largo = (relacion / largo_watermark) * 100
    else:
        print("Todo bien")
        nuevo_largo = largo_watermark
        nuevo_alto = alto_watermark
    print("Cambiando tamaño a{}x{}".format(nuevo_largo, nuevo_alto))
    marca_de_agua.thumbnail((nuevo_largo, nuevo_alto), Image.ANTIALIAS)
    print("Modificando opacidad de imagen...")
    #marca_de_agua.putalpha(OPACIDAD)
    print("Pegando marca de agua...")
    # Calcular variables para centrar
    x =int( largo_original - nuevo_largo)
    y =int( alto_original - nuevo_alto)
    imagen.paste(marca_de_agua, (x, y), marca_de_agua)
    print("X: {}, Y: {}".format(x, y))
    print("Alto original: {},alto de la marca: {} ".format(alto_original, nuevo_alto))
    print("Renombrando original...")

    # Renombrar


    #inicio, extension = os.path.splitext(ruta_absoluta_imagen_original)
    #nombre_imagen_respaldar = join(ruta_ubicacion_imagen, inicio + "_original" + extension)
    #os.rename(ruta_absoluta_imagen_original, nombre_imagen_respaldar)


    nombre_de_la_imagen_original = os.path.basename(ruta_imagen)
    nombre_imagen_guardar = join(ruta_guardado, nombre_de_la_imagen_original)
    print("Guardando como " + nombre_imagen_guardar)
    imagen.save(nombre_imagen_guardar)
    print("OK")