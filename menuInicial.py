import tkinter as tk
from juego import empezarJuego
from tkinter import PhotoImage
from configPartida import cargarConfigPartida

# Función que se ejecuta al hacer clic en el botón "Crear partida"
def onClickBtnCrearPartida(root):
    # Oculta el frame del menú inicial
    bgImagen.pack_forget()
    frameMenu.pack_forget()
    # Carga la configuración de la partida
    cargarConfigPartida(root)
    


# Función para cargar el estado del juego desde un archivo guardado
def onClickCargarPartida():
    nombreArchivo = "partida_guardada.txt"
    
    try:
        with open(nombreArchivo, 'r') as archivo:
            lineas = archivo.readlines()
            estadoJuego = {'turno': None, 'posicionesJ1': [], 'posicionesJ2': []}
            turno = None
            posicionesJ1 = []
            posicionesJ2 = []
            for linea in lineas:
                if linea.startswith("Turno:"):
                    turno = linea.split(":")[1].strip()
                    estadoJuego['turno'] = turno
                elif linea.startswith("Posicion de barcos para J1:"):
                    continue
                elif linea.startswith("Posicion de barcos para J2:"):
                    continue
                elif linea.strip():
                    partes = linea.strip().split(':')
                    barco = partes[0].strip()
                    posiciones = partes[1].strip().split('], [')
                    posicionesBarco = []
                    for pos in posiciones:
                        pos = pos.strip('[ ]')
                        x, y = map(int, pos.split(','))
                        posicionesBarco.append([x, y])
                    if turno == "J1":
                        posicionesJ1.append((barco, posicionesBarco))
                    elif turno == "J2":
                        posicionesJ2.append((barco, posicionesBarco))
            estadoJuego['posicionesJ1'] = posicionesJ1
            estadoJuego['posicionesJ2'] = posicionesJ2
            print("Partida cargada exitosamente.")
            # Llamada a la función empezarJuego con el estado cargado
            empezarJuego(estadoJuego)
            return estadoJuego
    except FileNotFoundError:
        print("No se encontró el archivo de partida guardada.")
        return None
    except Exception as e:
        onClickBtnCrearPartida(root)
        return None

    
    
# Función para cargar el menú inicial
def cargarMenuInicial(vtn):
    global frameMenu, root
    global bgImagen
    
    root = vtn
    
    # Crear el frame del menú
    frameMenu = tk.Frame(root)
    frameMenu.configure(background="light blue")
    frameMenu.pack(expand=True, fill="both")
        # Cargar la imagen de fondo
    imagemFondo = PhotoImage(file=r'Assets\IMAGEN1.png')
    bgImagen = tk.Label(root, image=imagemFondo)
    bgImagen.pack()
    bgImagen.place(x='60',y='270')

    # Importante: mantener una referencia de imagemFondo
    bgImagen.image = imagemFondo

    # Botón Crear Partida
    btnCrearPartida = tk.Button(frameMenu)
    btnCrearPartida.configure(
        text="CREAR PARTIDA",
        width=100,
        command=lambda: onClickBtnCrearPartida(root)  # Llama a la función onClickBtnCrearPartida con la ventana principal como argumento
    )
    btnCrearPartida.pack()
    btnCrearPartida.place(x=700, y=50, height=80)

    # Botón cargar partida
    btnCargar = tk.Button(frameMenu)
    btnCargar.configure(
        text="CARGAR PARTIDA",
        width=100,
        command=onClickCargarPartida
    )
    btnCargar.pack()
    btnCargar.place(x=700, y=140, height=80)
