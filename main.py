from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from PIL import Image
import time


OPCION_HORIZONTAL_IZQUIERDA = 0
OPCION_HORIZONTAL_DERECHA = 1
OPCION_HORIZONTAL_CENTRO = 2

OPCION_VERTICAL_ARRIBA = 0
OPCION_VERTICAL_ABAJO = 1
OPCION_VERTICAL_CENTRO = 2


raiz = Tk()
raiz.title("Poner marca de agua")
raiz.geometry("600x400")

opcion_horizontal = IntVar()
opcion_vertical = IntVar()
def seleccionar_marca_de_agua():
    marca_de_agua = filedialog.askopenfilename(parent=raiz, title="Selecciona tu marca de agua")
    if not es_extension_valida(obtener_extension(marca_de_agua)):
        print("Imagen inválida")
    else:
        raiz.marca_de_agua = marca_de_agua
        print("Imagen válida")

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    imagenes = obtener_lista_de_imagenes_en_directorio(directorio)
    procesar_lista_de_imagenes(imagenes)

def es_extension_valida(extension):
    return extension.lower() in [".jpg", ".png"]

def obtener_extension(archivo):
    archivo, extension = os.path.splitext(archivo)
    return extension

def obtener_lista_de_imagenes_en_directorio(directorio):
    imagenes = []
    for fichero_o_directorio in os.listdir(directorio):
        ruta_absoluta = os.path.join(directorio, fichero_o_directorio)
        if os.path.isfile(ruta_absoluta):
            if es_extension_valida(obtener_extension(ruta_absoluta)):
                imagenes.append(ruta_absoluta)
    return imagenes

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(parent=raiz, title="Selecciona las imágenes")
    procesar_lista_de_imagenes(archivos)

def ver_sitio_web_programador(a):
    print("*abre el sitio del programador*")

def ver_repositorio(a):
    print("*abre el repositorio*")

def procesar_lista_de_imagenes(imagenes):
    raiz.imagenes = imagenes

def obtener_x_segun_preferencias(anchura_marca_de_agua, anchura_imagen, posicion, separacion_horizontal):
    x = 0
    if posicion == OPCION_HORIZONTAL_IZQUIERDA:
        x = separacion_horizontal
    elif posicion == OPCION_HORIZONTAL_CENTRO:
        centro_imagen = anchura_imagen / 2
        centro_marca_de_agua = anchura_marca_de_agua / 2
        centro = centro_imagen - centro_marca_de_agua
        x = centro + separacion_horizontal
    elif posicion == OPCION_HORIZONTAL_DERECHA:
        x = anchura_imagen - separacion_horizontal - anchura_marca_de_agua
    return int(x)

def obtener_y_segun_preferencias(altura_marca_de_agua, altura_imagen, posicion, separacion_vertical):
    y = 0
    if posicion == OPCION_VERTICAL_ARRIBA:
        y = separacion_vertical
    elif posicion == OPCION_VERTICAL_CENTRO:
        centro_imagen = altura_imagen / 2
        centro_marca_de_agua = altura_marca_de_agua / 2
        centro = centro_imagen - centro_marca_de_agua
        y = centro + separacion_vertical
    elif posicion == OPCION_VERTICAL_ABAJO:
        y = altura_imagen - separacion_vertical - altura_marca_de_agua
    return int(y)
        

def poner_marca_de_agua():
    

    # Comprobar si tenemos imágenes y marca de agua
    if not hasattr(raiz, "imagenes"):
        messagebox.showinfo("Aviso", "No has seleccionado ninguna imagen")
        return
    if not hasattr(raiz, "marca_de_agua"):
        messagebox.showinfo("Aviso", "No has seleccionado la marca de agua")
        return

    # Leer los ajustes que el usuario puso
    porcentaje_opacidad = int(slider_rango_opacidad.get())
    separacion_vertical = int(entry_separacion_vertical.get())
    separacion_horizontal = int(entry_separacion_horizontal.get())
    opcion_alineamiento_horizontal = int(opcion_horizontal.get())
    opcion_alineamiento_vertical = int(opcion_vertical.get())

    # A trabajar. Le quitamos la opacidad a la imagen
    marca_de_agua = Image.open(raiz.marca_de_agua).convert("RGBA")
    anchura_marca_de_agua, altura_marca_de_agua = marca_de_agua.size
    for x in range(anchura_marca_de_agua):
        for y in range(altura_marca_de_agua):
            rgb = marca_de_agua.getpixel((x,y))
            k = (rgb[0],rgb[1],rgb[2],int((porcentaje_opacidad * rgb[3]) / 100))
            marca_de_agua.putpixel((x,y), k)
    # Una vez que la marca de agua esté lista, la pegamos sobre las demás
    ruta_imagen = raiz.imagenes[0]
    imagen = Image.open(ruta_imagen)
    anchura_imagen, altura_imagen = imagen.size
    x = obtener_x_segun_preferencias(anchura_marca_de_agua, anchura_imagen, opcion_alineamiento_horizontal, separacion_horizontal)
    y = obtener_y_segun_preferencias(altura_marca_de_agua, altura_imagen, opcion_alineamiento_vertical, separacion_vertical)
    imagen.paste(marca_de_agua, (x, y), marca_de_agua)
    nombre_imagen_guardada = "Salida_{}.png".format(time.time())
    imagen.save(nombre_imagen_guardada)
    print("Guardada como " + nombre_imagen_guardada)
    #for imagen in raiz.imagenes:
        #print("*procesa la imagen {}*".format(imagen))

etiqueta_ayuda = Label(raiz, text="1 - Selecciona un directorio o imagen...").grid(row=0, column=0)
btn_seleccionar_directorio = Button(raiz, text="Directorio/carpeta", command = seleccionar_directorio).grid(row=1,column=0)

btn_seleccionar_archivos = Button(raiz, text="Archivo (s)", command = seleccionar_archivos).grid(row=1, column=1)

etiqueta_marca_de_agua = Label(raiz, text="2 - Ahora selecciona la marca de agua:").grid(row=2,column=0)

btn_seleccionar_marca_de_agua = Button(raiz, text="Seleccionar marca de agua", command = seleccionar_marca_de_agua).grid(row=3,column=0)

slider_rango_opacidad = Scale(raiz, from_=0, to=100, label="3 - % opacidad", orient=HORIZONTAL)
slider_rango_opacidad.grid(row=4,column=0)

Label(raiz, text="4 - ¿En qué parte se debe poner la marca de agua?").grid(row=5)
Label(raiz, text="Horizontalmente:").grid(row=6, column=0)
Radiobutton(raiz, text="Izquierda", variable=opcion_horizontal, value=0).grid(row=7,column=0)
Radiobutton(raiz, text="Derecha", variable=opcion_horizontal, value=1).grid(row=7,column=2)
Radiobutton(raiz, text="Centro", variable=opcion_horizontal, value=2).grid(row=7,column=1)

Label(raiz, text="Verticalmente:").grid(row=8, column=0)
Radiobutton(raiz, text="Arriba", variable=opcion_vertical, value=0).grid(row=9,column=0)
Radiobutton(raiz, text="Abajo", variable=opcion_vertical, value=1).grid(row=9,column=2)
Radiobutton(raiz, text="Centro", variable=opcion_vertical, value=2).grid(row=9,column=1)

Label(raiz, text="Separación vertical en px").grid(row=10, column=0)

entry_separacion_vertical = Entry(raiz)
entry_separacion_vertical.grid(row=10, column=1)
entry_separacion_vertical.insert(0, "0")


Label(raiz, text="Separación horizontal en px").grid(row=11, column=0)

entry_separacion_horizontal = Entry(raiz)
entry_separacion_horizontal.grid(row=11, column=1)
entry_separacion_horizontal.insert(0, "0")

btn_poner_marca_de_agua = Button(raiz, text="Comenzar", command = poner_marca_de_agua).grid(row=15,column=0)
Label(raiz, text="Creado y mantenido por Parzibyte. Este programa es gratuito y open source").grid(row=16,column=0)


etiqueta_sitio_web_programador = Label(raiz, text="Sitio web del programador", fg="blue", cursor="hand2")
etiqueta_sitio_web_programador.grid(row=17,column=0)
etiqueta_sitio_web_programador.bind("<Button-1>", ver_sitio_web_programador)

etiqueta_repositorio = Label(raiz, text="Ver código fuente", fg="blue", cursor="hand2")
etiqueta_repositorio.grid(row=17,column=1)
etiqueta_repositorio.bind("<Button-1>", ver_repositorio)

opcion_vertical.set(OPCION_VERTICAL_ABAJO)
opcion_horizontal.set(OPCION_HORIZONTAL_DERECHA)
raiz.mainloop()