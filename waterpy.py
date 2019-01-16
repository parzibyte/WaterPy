from PIL import Image
import constantes
import time

def obtener_x(anchura_marca_de_agua, anchura_imagen, posicion, separacion_horizontal):
    x = 0
    if posicion == constantes.OPCION_HORIZONTAL_IZQUIERDA:
        x = separacion_horizontal
    elif posicion == constantes.OPCION_HORIZONTAL_CENTRO:
        centro_imagen = anchura_imagen / 2
        centro_marca_de_agua = anchura_marca_de_agua / 2
        centro = centro_imagen - centro_marca_de_agua
        x = centro + separacion_horizontal
    elif posicion == constantes.OPCION_HORIZONTAL_DERECHA:
        x = anchura_imagen - separacion_horizontal - anchura_marca_de_agua
    return int(x)

def obtener_y(altura_marca_de_agua, altura_imagen, posicion, separacion_vertical):
    y = 0
    if posicion == constantes.OPCION_VERTICAL_ARRIBA:
        y = separacion_vertical
    elif posicion == constantes.OPCION_VERTICAL_CENTRO:
        centro_imagen = altura_imagen / 2
        centro_marca_de_agua = altura_marca_de_agua / 2
        centro = centro_imagen - centro_marca_de_agua
        y = centro + separacion_vertical
    elif posicion == constantes.OPCION_VERTICAL_ABAJO:
        y = altura_imagen - separacion_vertical - altura_marca_de_agua
    return int(y)
        

def poner_marca_de_agua(imagenes, marca_de_agua, **opciones):   
    # Leer los ajustes que el usuario puso
    porcentaje_opacidad = opciones.get("porcentaje_opacidad")
    separacion_vertical = opciones.get("separacion_vertical")
    separacion_horizontal = opciones.get("separacion_horizontal")
    opcion_alineamiento_horizontal = opciones.get("opcion_alineamiento_horizontal")
    opcion_alineamiento_vertical = opciones.get("opcion_alineamiento_vertical")
    
    # A trabajar. Le quitamos la opacidad a la imagen
    marca_de_agua = Image.open(marca_de_agua).convert("RGBA")
    anchura_marca_de_agua, altura_marca_de_agua = marca_de_agua.size
    for x in range(anchura_marca_de_agua):
        for y in range(altura_marca_de_agua):
            rgba = marca_de_agua.getpixel((x,y))
            nuevo_rgba = (rgba[0],rgba[1],rgba[2],int((porcentaje_opacidad * rgba[3]) / 100))
            marca_de_agua.putpixel((x,y), nuevo_rgba)
    # Una vez que la marca de agua esté lista, la pegamos sobre las demás
    ruta_imagen = imagenes[0]
    imagen = Image.open(ruta_imagen)
    anchura_imagen, altura_imagen = imagen.size
    x = obtener_x(anchura_marca_de_agua, anchura_imagen, opcion_alineamiento_horizontal, separacion_horizontal)
    y = obtener_y(altura_marca_de_agua, altura_imagen, opcion_alineamiento_vertical, separacion_vertical)
    imagen.paste(marca_de_agua, (x, y), marca_de_agua)
    nombre_imagen_guardada = "Salida_{}.png".format(time.time())
    imagen.save(nombre_imagen_guardada)
    print("Guardada como " + nombre_imagen_guardada)
    #for imagen in raiz.imagenes:
        #print("*procesa la imagen {}*".format(imagen))