import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# VARIABLES
matrizJuego = []
destructoresJ1 = []
crucerosJ1 = []
acorazadosJ1 = []
cantFilas = 0
cantColumn = 0
turno = "J1"

# FUNCIONES
def onClickBtnCrearPartida():
    frameMenu.pack_forget()
    frameConfig.pack(expand=True, fill="both")

def onClickBtnJugar():
    global cantColumn, cantFilas
    nickNameJ1 = ""
    nickNameJ2 = ""
    

    if entryJugador1.get() != entryJugador2.get(): #Se comprueba que los nicknames sean diferentes.
        nickNameJ1 =  entryJugador1.get()
        nickNameJ2 =  entryJugador2.get()

        if int(entryFila.get()) >= 10: #Se comprueba que la fila sea mayor o igual a 10.
            cantFilas = int(entryFila.get())

            if int(entryColumna.get()) >= 20: #Se comprueba que la columna sea mayor o igual a 20.
                cantColumn = int(entryColumna.get())
                #Se cambia al fram de juego
                frameConfig.pack_forget()
                empezarJuego(cantFilas, cantColumn)
            else:
                messagebox.showinfo("Alerta", "¡Debe tener 20 columnas o más!")
        else:
            messagebox.showinfo("Alerta", "¡Debe tener 10 filas o más!")

    else: 
        messagebox.showinfo("Alerta", "¡Los nicknames deben ser diferentes!")

def empezarJuego(filas, columnas):
    global matrizJuego
    
    frameJuego.pack(expand=True, fill="both")
   
    for fila in range(filas):
        submatrizJuego = [] 

        frameJuego.rowconfigure(fila, weight=1)

        for columna in range(columnas * 2):
            frameJuego.columnconfigure(columna, weight=1)

            celda = tk.Button(frameJuego, command= lambda x=fila, y=columna: onClickCelda(x,y), 
                              text=f"{fila}-{columna}")
            celda.configure(fg="white")
            if columna >= columnas:
                celda.configure(background="red")
            else:
                celda.configure(background="blue")

            celda.grid(row=fila, column=columna, sticky="nsew")
            submatrizJuego.append(celda)

        matrizJuego.append(submatrizJuego)
    deshabilitarTablero(2)


def deshabilitarTablero(jugador):
    global cantColumn

    print("Entramos a la función")
    print(matrizJuego)

    for fila in matrizJuego:
        print(f"Estamos en la fila: {fila}")
        cont = 0
        for boton in fila:  # Itera sobre los botones en la fila, no sobre los índices
            print(f"Boton: {boton}")
            if jugador == 1:
                if cont < cantColumn:
                    print(f"{1} : {cont}")
                    boton.configure(state="disabled")
            elif jugador == 2:
                if cont >= cantColumn:  # Se corrigió el operador de comparación
                    print(f"{2} : {cont}")
                    boton.configure(state="disabled")
            cont += 1

def habilitarTablero(jugador):
    global cantColumn

    print("Entramos a la función")
    print(matrizJuego)

    for fila in matrizJuego:
        print(f"Estamos en la fila: {fila}")
        cont = 0
        for boton in fila:  # Itera sobre los botones en la fila, no sobre los índices
            print(f"Boton: {boton}")
            if jugador == 1:
                if cont < cantColumn:
                    print(f"{1} : {cont}")
                    boton.configure(state="normal")
            elif jugador == 2:
                if cont >= cantColumn:  # Se corrigió el operador de comparación
                    print(f"{2} : {cont}")
                    boton.configure(state="normal")
            cont += 1

def onClickCelda(fila, columna):
    global destructoresJ1
    
    # Crear una nueva ventana para el pop-up
    popup = tk.Toplevel()
    popup.title("Posicionar barco.")

    # Variables para almacenar la selección del usuario
    tipo_barco = tk.StringVar()
    direccion = tk.StringVar()
    
    # Etiqueta y opciones para seleccionar el tipo de barco
    label_barco = tk.Label(popup, text="Seleccionar tipo de barco:")
    label_barco.pack()
    barco_opciones = tk.OptionMenu(popup, tipo_barco, "Destructor", "Crucero", "Acorazado")
    barco_opciones.pack()

    # Etiqueta y opciones para seleccionar la dirección
    label_direccion = tk.Label(popup, text="Seleccionar dirección:")
    label_direccion.pack()
    direccion_opciones = tk.OptionMenu(popup, direccion, "Horizontal", "Vertical")
    direccion_opciones.pack()

    # Función para manejar el botón "Aceptar"
    def aceptar():
        seleccion_barco = tipo_barco.get()
        seleccion_direccion = direccion.get()
        if seleccion_barco == "": #Validamos que no hayan datos vacios.
            label_barco.configure(text="Debe seleccionar un barco:", fg="red")
        elif seleccion_direccion == "":
            label_direccion.configure(text="Debe seleccionar una dirección:", fg="red")
        else: #Posicionar barco
            if turno == "J1":
                #AGREGAR BARCOS PARA J1
                #Agregar un destructor
                if seleccion_barco == "Destructor" and len(destructoresJ1) < 6:
                    if seleccion_direccion == "Vertical":
                        destructoresJ1.append([[fila, columna], "V"]) #Agrega al destructor a la lista
                        matrizJuego[fila][columna].configure(image = destructor_ver) #Mostrar al destructor
                    else:
                        destructoresJ1.append([[fila, columna], "H"]) #Agrega al destructor a la lista
                        matrizJuego[fila][columna].configure(image = destructor_hor) #Mostrar al destructor
                    print(len(destructoresJ1), destructoresJ1)
                    
                #Agregar un crucero
                elif seleccion_barco == "Crucero" and len(crucerosJ1) < 4:
                    if seleccion_direccion == "Vertical":
                        crucerosJ1.append([[fila, columna], "V"]) #Agrega al crucero a la lista
                        
                        #Mostrar el crucero
                        matrizJuego[fila][columna].configure(image = crucero_ver[0])
                        matrizJuego[fila+1][columna].configure(image = crucero_ver[1])
                    else:
                        crucerosJ1.append([[fila, columna], "H"]) #Agrega al crucero a la lista
                        
                        #Mostrar el crucero
                        matrizJuego[fila][columna].configure(image = crucero_hor[0])
                        matrizJuego[fila][columna-1].configure(image = crucero_hor[1])
                    print(len(crucerosJ1), crucerosJ1)
                #Agregar acorazado
                elif seleccion_barco == "Acorazado" and len(acorazadosJ1) < 2: 
                    if seleccion_direccion == "Vertical":
                        acorazadosJ1.append([[fila, columna], "V"]) #Agrega al acorazado a la lista
                        
                        #Mostrar el acorazado
                        matrizJuego[fila][columna].configure(image = acorazado_ver[0])
                        matrizJuego[fila+1][columna].configure(image = acorazado_ver[1])
                        matrizJuego[fila+2][columna].configure(image = acorazado_ver[2])
                    else:
                        acorazadosJ1.append([[fila, columna], "H"]) #Agrega al acorazado a la lista
                        
                        #Mostrar el acorazado
                        matrizJuego[fila][columna].configure(image = acorazado_hor[0])
                        matrizJuego[fila][columna-1].configure(image = acorazado_hor[1])
                        matrizJuego[fila][columna-2].configure(image = acorazado_hor[2])
                    print(len(acorazadosJ1), acorazadosJ1)
                elif turno == "J2":
                    #Implementar código para agregar los barcos del jugador dos (copiar el del J1 pero modificar y crear las listas para que sean para el J2)
                    pass
            popup.destroy()
            
        if len(destructoresJ1) == 6 and len(crucerosJ1) == 4 and len(acorazadosJ1) == 2:
            deshabilitarTablero(1)
            habilitarTablero(2)
            turno = "J2"

    # Botón para aceptar la selección
    tk.Button(popup, text="Aceptar", command=aceptar).pack()

# Abre la imagen
def imagenes():
    global destructor_ver, destructor_hor
    global crucero_ver, crucero_hor
    global acorazado_hor, acorazado_ver
    
    # DESTRUCTOR-----------------------------------------------------------
    destructor_hor = Image.open(r"assets\destructor.png")
    destructor_hor = destructor_hor.resize((40, 40))
    destructor_hor = ImageTk.PhotoImage(destructor_hor)
    
    destructor_ver = Image.open(r"assets\destructor.png")
    destructor_ver = destructor_ver.resize((40, 40))
    destructor_ver = destructor_ver.rotate(90)
    destructor_ver = ImageTk.PhotoImage(destructor_ver)

    # CRUCERO---------------------------------------------------------------
    crucero_hor = []
    crucero_ver = []
    
    #Importamos las partes
    crucero1 = Image.open(r"assets\crucero1.png")
    crucero1 = crucero1.resize((40, 40))
    crucero2 = Image.open(r"assets\crucero2.png")
    crucero2 = crucero2.resize((40, 40))
    
    #Almacenar las imágenes
    crucero_hor.append(ImageTk.PhotoImage(crucero1))
    crucero_hor.append(ImageTk.PhotoImage(crucero2))
    
    crucero1 = crucero1.rotate(90)
    crucero2 = crucero2.rotate(90)
    
    crucero_ver.append(ImageTk.PhotoImage(crucero1))
    crucero_ver.append(ImageTk.PhotoImage(crucero2))
    
    # ACORAZADO ----------------------------------------------------
    acorazado_hor = []
    acorazado_ver = []
    
    acorazado1 = Image.open(r"assets\acorazado1.png")
    acorazado1 = acorazado1.resize((40, 40))
    acorazado2 = Image.open(r"assets\acorazado2.png")
    acorazado2 = acorazado2.resize((40, 40))
    acorazado3 = Image.open(r"assets\acorazado3.png")
    acorazado3 = acorazado3.resize((40, 40))
    
    #Almacenar las imágenes verticales
    acorazado_ver.append(ImageTk.PhotoImage(acorazado1))
    acorazado_ver.append(ImageTk.PhotoImage(acorazado2))
    acorazado_ver.append(ImageTk.PhotoImage(acorazado3))

    #Rotar Imágenes 
    acorazado1 = acorazado1.rotate(90)
    acorazado2 = acorazado2.rotate(90)
    acorazado3 = acorazado3.rotate(90)
    
    #Almacenar las imágenes horizontales
    acorazado_hor.append(ImageTk.PhotoImage(acorazado3))
    acorazado_hor.append(ImageTk.PhotoImage(acorazado2))
    acorazado_hor.append(ImageTk.PhotoImage(acorazado1))
    
    



# INTERFAZ
# Ventana principal
root = tk.Tk()
root.title('BattleShip')
screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())

# Establecer el tamaño de la ventana para que coincida con las dimensiones de la pantalla
root.geometry(f"{screen_width}x{screen_height}")

root.resizable(True, True)
root.configure(background="red")

# Frame menú
frameMenu = tk.Frame(root)
frameMenu.configure(background="blue")
frameMenu.pack(expand=True, fill="both")

# Botón Crear Partida
btnCrearPartida = tk.Button(frameMenu)
btnCrearPartida.configure(
    text="Crear partida.",
    width=30,
    command=lambda: onClickBtnCrearPartida()
)
btnCrearPartida.pack()
btnCrearPartida.place(x=150, y=250, height=30)

# Botón cargar partida
btnCargar = tk.Button(frameMenu)
btnCargar.configure(
    text="Cargar Partida",
    width=30,
)
btnCargar.pack()
btnCargar.place(x=150, y=300, height=30)

# Frame CONFIGURACIONES
frameConfig = tk.Frame(root)
frameConfig.configure(background="green")

# Entry JUGADOR 1
# Label
labelJugador1 = tk.Label(frameConfig)
labelJugador1.configure(
    text="Nickname Jugador 1",
    width=30,
)
labelJugador1.pack()
labelJugador1.place(x=150, y=50, height=30)

# Entry
entryJugador1 = tk.Entry(frameConfig)
entryJugador1.configure(
    width=35
)
entryJugador1.pack()
entryJugador1.place(x=151, y=100, height=30)

# Entry JUGADOR 2
# Label
labelJugador2 = tk.Label(frameConfig)
labelJugador2.configure(
    text="Nickname Jugador 2",
    width=30,
)
labelJugador2.pack()
labelJugador2.place(x=150, y=150, height=30)

# Entry
entryJugador2 = tk.Entry(frameConfig)
entryJugador2.configure(
    width=35,
)
entryJugador2.pack()
entryJugador2.place(x=151, y=200, height=30)

# Cantidad filas/columanas
# Label FILA
labelFila = tk.Label(frameConfig)
labelFila.configure(
    text="Ingrese la cantidad de filas:",
    width=30
)
labelFila.pack()
labelFila.place(x=150, y=250, height=30)

# Entry FILA
entryFila = tk.Entry(frameConfig)
entryFila.configure(
    width=35
)
entryFila.pack()
entryFila.place(x=151, y=300, height=30)

# Label COLUMNA
labelColumna = tk.Label(frameConfig)
labelColumna.configure(
    text="Ingrese la cantidad de columnas:",
    width=30
)
labelColumna.pack()
labelColumna.place(x=150, y=350, height=30)

# Entry COLUMNA
entryColumna = tk.Entry(frameConfig)
entryColumna.configure(
    width=35
)
entryColumna.pack()
entryColumna.place(x=151, y=400, height=30)

# Botón Jugar
btnJugar = tk.Button(frameConfig)
btnJugar.configure(
    text="Jugar",
    command=lambda: onClickBtnJugar(),
    width=30
)
btnJugar.pack()
btnJugar.place(x=150, y=450, height=30)

# Frame JUEGO
frameJuego = tk.Frame(root)

#Cargar imagenes
imagenes()

# Bucle para que se mantenga abierto
root.mainloop()
