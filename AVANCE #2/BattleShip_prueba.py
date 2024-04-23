import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# VARIABLES
matrizJuego = []
destructores = []
imgDestructores = []

# FUNCIONES
def onClickBtnCrearPartida():
    frameMenu.pack_forget()
    frameConfig.pack(expand=True, fill="both")

def onClickBtnJugar():
    nickNameJ1 = ""
    nickNameJ2 = ""
    cantFilas = 0
    cantColumn = 0

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
    frameJuego.pack(expand=True, fill="both")
    alturaBtn = screen_height / filas
    anchoBtn = screen_width / columnas

    posy = 0
   
    for fila in range(filas):
        submatrizJuego = [] 

        frameJuego.rowconfigure(fila, weight=1)

        posx = 0
        for columna in range(columnas * 2):
            frameJuego.columnconfigure(columna, weight=1)

            celda = tk.Button(frameJuego, command= lambda x=fila, y=columna: onClickCelda(x,y), 
                              text=f"{fila} - {columna}")
            celda.configure(fg="white")
            if columna >= columnas:
                celda.configure(background="red")
            else:
                celda.configure(background="blue")

            celda.grid(row=fila, column=columna, sticky="nsew")
            submatrizJuego.append(celda)
            posx += anchoBtn

        matrizJuego.append(submatrizJuego)
        posy += alturaBtn

def onClickCelda(x, y):
    global destructores, destructor, imgDestructores

    xyDestructores = []
    for d in destructores: 
        xyDestructores.append(d[0])

    if [x, y] in xyDestructores:
        print(f"Barco ya colocado: {x, y}")
        #Variables 
        indiceBarco = xyDestructores.index([x,y])
        grado = destructores[indiceBarco][1]
        print(grado)
        #Rotación del barco
        grado += 90
        destructorRotado = Image.open(r"assets\destructor.png")
        destructorRotado = destructorRotado.resize((40, 40))
        destructorRotado = destructorRotado.rotate(grado)
        imgDestructores[indiceBarco] = ImageTk.PhotoImage(destructorRotado)
    
        print(destructores)
        #Actualizar imagen
        matrizJuego[x][y].configure(image=imgDestructores[indiceBarco])
    else:
        if len(destructores) < 4:
            imgDestructores.append(destructor)
            matrizJuego[x][y].configure(image=imgDestructores[-1])
            destructores.append([[x, y], 0])
    pass
            

# Abre la imagen
def imagenes():
    global destructor
    global crucero1
    global crucero2
    
    # Destructor
    destructor = Image.open(r"assets\destructor.png")
    destructor = destructor.resize((40, 40))
    destructor = destructor.rotate(180)
    destructor = ImageTk.PhotoImage(destructor)

    # Crucero
    crucero1 = Image.open(r"assets\crucero1.png")
    crucero1 = crucero1.resize((40, 40))
    crucero1 = crucero1.rotate(180)
    crucero1 = ImageTk.PhotoImage(crucero1)

    crucero2 = Image.open(r"assets\crucero2.png")
    crucero2 = crucero2.resize((40, 40))
    crucero2 = crucero2.rotate(180)
    crucero2 = ImageTk.PhotoImage(crucero2)

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

# Botón jugar
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
frameJuego.configure(
    background="#ADD8E6",
    width=screen_width,
    height=screen_height
    )

#Cargar imagenes
imagenes()
# Bucle para que se mantenga abierto
root.mainloop()
