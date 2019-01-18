from appJar import gui
import constantes
import utiles
import waterpy
raiz = {}


def seleccionar_marca_de_agua():
    if "marca_de_agua" in raiz:
        del raiz["marca_de_agua"]
    marca_de_agua = app.openBox(title="Selecciona la marca de agua", dirName=None, fileTypes=None, asFile=False, parent=None)
    print("A ver la marca de agua:", marca_de_agua)
    if utiles.es_extension_valida(utiles.obtener_extension(marca_de_agua)):
        raiz["marca_de_agua"] = marca_de_agua
        app.setMessage("msgInfoMarca", "OK: " + marca_de_agua)
    else:
        app.setMessage("msgInfoMarca", "Marca de agua inválida")

def seleccionar_carpeta():
    if "imagenes" in raiz:
        del raiz["imagenes"]
    directorio = app.directoryBox(title="Selecciona una carpeta con imágenes", dirName=None, parent=None)
    print("A ver el directorio:", directorio)
    if directorio is not None:
        imagenes = utiles.obtener_lista_de_imagenes_en_directorio(directorio)
        procesar_lista_de_imagenes(imagenes)
        app.setMessage("msgInfoFuente", "OK: {}\nSe creará una carpeta en esa ubicación, y las imágenes marcadas serán colocadas dentro".format(directorio) )
    else:
        app.setMessage("msgInfoFuente", "Directorio inválido")

def seleccionar_imagen():
    if "imagenes" in raiz:
        del raiz["imagenes"]
    imagen = app.openBox(title="Selecciona la imagen", dirName=None, fileTypes=None, asFile=False, parent=None)
    print("A ver la imagen: '{}'".format(imagen))
    if utiles.es_extension_valida(utiles.obtener_extension(imagen)):
        procesar_lista_de_imagenes([imagen])
        app.setMessage("msgInfoFuente", "OK: " + imagen)        
    else:
        app.setMessage("msgInfoFuente", "Imagen inválida")        

def mostrar_creditos():
    
    app.showSubWindow("Créditos")

def poner_marca_de_agua():
    if validar():
        argumentos = {
            "porcentaje_opacidad": int(app.getScale("3 - Porcentaje de opacidad")),
            "separacion_vertical": int(app.getEntry("e1")),
            "separacion_horizontal": int(app.getEntry("e2")),
            "opcion_alineamiento_horizontal": app.getRadioButton("separacion_horizontal"),
            "opcion_alineamiento_vertical": app.getRadioButton("separacion_vertical"),
        }
        waterpy.poner_marca_de_agua(raiz["imagenes"], raiz["marca_de_agua"], **argumentos)

def validar():
    # Comprobar si tenemos imágenes y marca de agua
    if not "imagenes" in raiz:
        app.warningBox("Aviso", "No has seleccionado ninguna imagen o carpeta", parent=None)
        return False
    if not "marca_de_agua" in raiz:
        app.warningBox("Aviso", "No has seleccionado la marca de agua", parent=None)
        return False

    try:
        valor = int(app.getEntry("e1"))
    except ValueError:
        app.warningBox("Aviso", "Escribe la separación vertical en pixeles, o déjala en 0", parent=None)
        return False

    try:
        valor = int(app.getEntry("e2"))
    except ValueError:
        app.warningBox("Aviso", "Escribe la separación horizontal en pixeles, o déjala en 0", parent=None)
        return False
    return True

def procesar_lista_de_imagenes(imagenes):
    raiz["imagenes"] = imagenes

app = gui("WaterPy | Poner marca de agua con Python", "600x400")
"""
    Otra ventana para créditos
"""
app.startSubWindow("Créditos",modal=True)
app.setFont(12)
app.addMessage("creditos", """Aplicación para poner marcas de agua usando Python, PIL y appJar

Creada por @parzibyte

Este programa es totalmente gratuito y open source

Iconos usados
Icons made by Smashicons [https://www.flaticon.com/authors/smashicons] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

Icons made by Smashicons [https://www.flaticon.com/authors/smashicons] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

Icons made by surang [https://www.flaticon.com/authors/surang] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

Icons made by Maxim Basinski [https://www.flaticon.com/authors/maxim-basinski] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]
""")
app.addWebLink("Web del programador", "https://parzibyte.me", 1, 0)
app.addWebLink("Código en GitHub", "https://github.com/parzibyte/waterpy", 2, 0)
app.addWebLink("Página de WaterPy", "http://appsperfectas.com/apps/waterpy", 3, 0)
app.stopSubWindow()

"""
    Ahora sí la principal
"""
app.addLabel("l1", "1 - Selecciona una imagen o carpeta", 0,0)
app.setLabelAlign("l1", "left")
app.addNamedButton("Carpeta", "btnCarpeta", seleccionar_carpeta, 1, 0)
app.setButtonImage("btnCarpeta", "./assets/carpeta.png", align="right")
app.addNamedButton("Imagen", "btnImagen", seleccionar_imagen,1,1)
app.setButtonImage("btnImagen", "./assets/imagen.png", align="right")
app.addMessage("msgInfoFuente", "", 2,0)
app.setMessageFg("msgInfoFuente", "#304FFE")
app.setMessageAlign("msgInfoFuente", "left")
app.setMessageWidth("msgInfoFuente", 350)
app.addLabel("l2", "2 - Ahora selecciona la marca de agua", 3,0)
app.setLabelAlign("l2", "left")
app.addNamedButton("Seleccionar marca de agua...", "btnMarcaDeAgua", seleccionar_marca_de_agua,4,0)

app.setButtonImage("btnMarcaDeAgua", "./assets/lapiz.png", align="right")

app.addMessage("msgInfoMarca", "", 5,0)
app.setMessageAlign("msgInfoMarca", "left")
app.setMessageWidth("msgInfoMarca", 350)
app.setMessageFg("msgInfoMarca", "#304FFE")
app.addLabelScale("3 - Porcentaje de opacidad", 6,0)
app.setScaleRange("3 - Porcentaje de opacidad", 0, 100, 50)
app.showScaleValue("3 - Porcentaje de opacidad", True)
app.setScaleIncrement("3 - Porcentaje de opacidad", 1)
app.addLabel("l3", "4 - Posición de la marca de agua",7,0)
app.setLabelAlign("l3", "left")
app.addLabel("l4", "Horizontal",8,0)
app.setLabelAlign("l4", "center")
app.addRadioButton("separacion_horizontal", constantes.OPCION_HORIZONTAL_IZQUIERDA, 9, 0)
app.addRadioButton("separacion_horizontal", constantes.OPCION_HORIZONTAL_DERECHA, 10, 0)
app.addRadioButton("separacion_horizontal", constantes.OPCION_HORIZONTAL_CENTRO, 11, 0)
app.addLabel("l5", "Vertical",8,1)
app.setLabelAlign("l5", "center")
app.addRadioButton("separacion_vertical", constantes.OPCION_VERTICAL_ARRIBA, 9, 1)
app.addRadioButton("separacion_vertical", constantes.OPCION_VERTICAL_CENTRO, 10, 1)
app.addRadioButton("separacion_vertical", constantes.OPCION_VERTICAL_ABAJO, 11, 1)
app.addLabel("l6", "Separación vertical en px",12,0)
app.setLabelAlign("l6", "left")
app.addEntry("e1", 12, 1)
app.setEntry("e1", "0")
app.setEntryAlign("e1", "left")
app.addLabel("l7", "Separación horizontal en px",13,0)
app.setLabelAlign("l7", "left")
app.addEntry("e2", 13, 1)
app.setEntry("e2", "0")
app.addNamedButton("Comenzar", "btnComenzar", poner_marca_de_agua,14,0)
app.setButtonImage("btnComenzar", "./assets/iniciar.png", align="right")
app.addNamedButton("Acerca de", "btnCreditos", mostrar_creditos,14,1)
app.go()