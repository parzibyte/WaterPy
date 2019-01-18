# WaterPy
![WaterPy: poner marcas de agua con Python](https://raw.githubusercontent.com/parzibyte/WaterPy/master/assets/ImagenV1.png)

Una aplicación de escritorio (multiplataforma) para poner marcas de agua usando Python, PIL y appJar (una envoltura de Tkinter)
## Motivación
Personalmente necesito poner marcas de agua cuando subo algunas imágenes a mi web en [parzibyte.me/blog](https://parzibyte.me/blog). 

Hace tiempo tenía un script que hacía eso (para uso personal) pero no tenía interfaz ni opciones como alineación u opacidad
## Bugs y características
Si quieres, reporta un bug o pide una característica (que ayude a todos) en **Issues**

## Descargar
Puedes descargar la app (bueno, seguramente tiene otro nombre pero ya a todo se le dice app en estos días) en la página de **releases**;  actualmente está compilada para Windows pero debería servir en otras plataformas si tú la compilas (*o si yo consigo una PC con otro SO*)
## Probar código
Si eres un desarrollador, simplemente clona o descarga el repositorio, [instala Python y PIP](https://parzibyte.me/blog/2017/11/19/instalar-configurar-python-3-windows-10/) para más tarde instalar las dependencias:
```
pip install Pillow
pip install appjar
```

Después de eso simplemente ejecuta:
```
python interfaz.py
```
¡Y listo! :)
## Compilar
Instala PyInstaller y aprende a usarlo, para ello lee estos dos posts:

 1. [Compilar a ejecutable un archivo de Python](https://parzibyte.me/blog/2018/03/23/empaquetando-python-generar-archivo-exe/)
    
2. [Agregar assets a archivo ejecutable de Python](https://parzibyte.me/blog/2018/12/27/pyinstaller-assets-imagenes-archivos-ejecutable-python/)

Luego añade al archivo **spec** lo siguiente
```python
a.datas += [("./assets/carpeta.png", "./assets/carpeta.png", "DATA"),("./assets/imagen.png", "./assets/imagen.png", "DATA"),("./assets/iniciar.png", "./assets/iniciar.png", "DATA"),("./assets/lapiz.png", "./assets/lapiz.png", "DATA"),]
```
Y vuelve a compilar con:
```
pyinstaller --onefile interfaz.spec
```

# Agradecimientos
Gracias a los creadores de Python, PyInstaller, PIL, appJar y Tkinter

# Créditos
El programa está bajo la licencia MIT, puedes ver más en el apartado de la licencia. Creado y mantenido por [parzibyte](https://parzibyte.me)

Algunos (o todos, al momento de escribir esto) iconos son de flaticon.com:

Icons made by Smashicons [https://www.flaticon.com/authors/smashicons] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

  

Icons made by Smashicons [https://www.flaticon.com/authors/smashicons] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

  

Icons made by surang [https://www.flaticon.com/authors/surang] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]

  

Icons made by Maxim Basinski [https://www.flaticon.com/authors/maxim-basinski] from Flaticon [https://www.flaticon.com] is licensed by CC 3.0 BY [http://creativecommons.org/licenses/by/3.0/]