from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import constantes
import utiles
import waterpy
raiz = Tk()

raiz.title("Poner marca de agua")
raiz.geometry("600x400")

opcion_horizontal = IntVar()
opcion_vertical = IntVar()


def seleccionar_marca_de_agua():
    marca_de_agua = filedialog.askopenfilename(parent=raiz, title="Selecciona tu marca de agua")
    if utiles.es_extension_valida(utiles.obtener_extension(marca_de_agua)):
        raiz.marca_de_agua = marca_de_agua

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    imagenes = utiles.obtener_lista_de_imagenes_en_directorio(directorio)
    procesar_lista_de_imagenes(imagenes)

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(parent=raiz, title="Selecciona las imágenes")
    procesar_lista_de_imagenes(archivos)

def poner_marca_de_agua():
    if validar():
        argumentos = {
            "porcentaje_opacidad": int(slider_rango_opacidad.get()),
            "separacion_vertical": int(entry_separacion_vertical.get()),
            "separacion_horizontal": int(entry_separacion_horizontal.get()),
            "opcion_alineamiento_horizontal": int(opcion_horizontal.get()),
            "opcion_alineamiento_vertical": int(opcion_vertical.get()),
        }
        waterpy.poner_marca_de_agua(raiz.imagenes, raiz.marca_de_agua, **argumentos)

def validar():
    # Comprobar si tenemos imágenes y marca de agua
    if not hasattr(raiz, "imagenes"):
        messagebox.showinfo("Aviso", "No has seleccionado ninguna imagen")
        return False
    if not hasattr(raiz, "marca_de_agua"):
        messagebox.showinfo("Aviso", "No has seleccionado la marca de agua")
        return False
    return True

def ver_sitio_web_programador(a):
    utiles.ver_sitio_web_programador()

def ver_repositorio(a):
    utiles.ver_repositorio()

def procesar_lista_de_imagenes(imagenes):
    raiz.imagenes = imagenes




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

opcion_vertical.set(constantes.OPCION_VERTICAL_ABAJO)
opcion_horizontal.set(constantes.OPCION_HORIZONTAL_DERECHA)
raiz.mainloop()


raiz.mainloop()