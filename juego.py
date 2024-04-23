import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

def cambiarTurnoPosicionar():
    global turno
    
    if turno == "J1": #Se le da el turno a J2
        turno = "J2"
        frameJ2.grid(column = 0, columnspan= 3, row = 0, rowspan = 2, sticky="nsew")
        frameJ1.grid_remove()
    elif turno == "J2": #Se le da el turno a J2
        turno = "J1"
        frameJ1.grid(column = 0, columnspan= 3, row = 0, rowspan = 2, sticky="nsew")
        frameJ2.grid_remove()

def posicionarBarco(seleccion_barco, seleccion_direccion, fila, columna):
    global turno

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
            if len(destructoresJ1) == 6:
                 messagebox.showinfo("Mensaje", "Todos los destructores han sido añadidos.")
                    
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
            if len(crucerosJ1) == 4:
                 messagebox.showinfo("Mensaje", "Todos los cruceros han sido añadidos.")
            
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
            if len(acorazadosJ1) == 2:
                 messagebox.showinfo("Mensaje", "Todos los acorazados han sido añadidos.")
        
        if len(destructoresJ1) >= 6 and len(crucerosJ1) >= 4 and len(acorazadosJ1) >= 2:
            cambiarTurnoPosicionar()
        
        
    elif turno == "J2":
        #AGREGAR BARCOS PARA J1
        #Agregar un destructor
        if seleccion_barco == "Destructor" and len(destructoresJ2) < 6:
            if seleccion_direccion == "Vertical":
                destructoresJ2.append([[fila, columna], "V"]) #Agrega al destructor a la lista
                matrizJuego[fila][columna].configure(image = destructor_ver) #Mostrar al destructor
            else:
                destructoresJ2.append([[fila, columna], "H"]) #Agrega al destructor a la lista
                matrizJuego[fila][columna].configure(image = destructor_hor) #Mostrar al destructor
            if len(destructoresJ2) == 6:
                 messagebox.showinfo("Mensaje", "Todos los destructores han sido añadidos.")       
        #Agregar un crucero
        elif seleccion_barco == "Crucero" and len(crucerosJ2) < 4:
            if seleccion_direccion == "Vertical":
                crucerosJ2.append([[fila, columna], "V"]) #Agrega al crucero a la lista
                        
                #Mostrar el crucero
                matrizJuego[fila][columna].configure(image = crucero_ver[0])
                matrizJuego[fila+1][columna].configure(image = crucero_ver[1])
            else:
                crucerosJ2.append([[fila, columna], "H"]) #Agrega al crucero a la lista
                        
                #Mostrar el crucero
                matrizJuego[fila][columna].configure(image = crucero_hor[0])
                matrizJuego[fila][columna-1].configure(image = crucero_hor[1])
            if len(acorazadosJ2) == 4:
                 messagebox.showinfo("Mensaje", "Todos los acorazados han sido añadidos.")
        #Agregar acorazado
        elif seleccion_barco == "Acorazado" and len(acorazadosJ2) < 2: 
            if seleccion_direccion == "Vertical":
                acorazadosJ2.append([[fila, columna], "V"]) #Agrega al acorazado a la lista
                        
                #Mostrar el acorazado
                matrizJuego[fila][columna].configure(image = acorazado_ver[0])
                matrizJuego[fila+1][columna].configure(image = acorazado_ver[1])
                matrizJuego[fila+2][columna].configure(image = acorazado_ver[2])
            else:
                acorazadosJ2.append([[fila, columna], "H"]) #Agrega al acorazado a la lista
                        
                #Mostrar el acorazado
                matrizJuego[fila][columna].configure(image = acorazado_hor[0])
                matrizJuego[fila][columna-1].configure(image = acorazado_hor[1])
                matrizJuego[fila][columna-2].configure(image = acorazado_hor[2])
            if len(acorazadosJ2) == 2:
                 messagebox.showinfo("Mensaje", "Todos los destructores han sido añadidos.")
                 # el juego inicia una vez el J2 haya finalizado
        if len(destructoresJ2) >= 6 and len(crucerosJ2) >= 4 and len(acorazadosJ2) >= 2:
            cambiarTurnoPosicionar()
            empezarJuego()
       


# Abre la imagen
def imagenes():
    global destructor_ver, destructor_hor
    global crucero_ver, crucero_hor
    global acorazado_hor, acorazado_ver
    global imgTransparente
    
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
    
    #Imagen Transparente
    imgTransparente = tk.PhotoImage() 
    
    
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


def onClickCelda(fila, columna):
    if (columna >= 0 and columna <= cantColumn - 1) and turno == "J1": #Tablero jugador 1
        if len(destructoresJ1) < 6 or len(crucerosJ1) < 4 or len(acorazadosJ1) < 2:
            # Crear una nueva ventana para el pop-up
            popup = tk.Toplevel()
            popup.title("Posicionar barco.")

            # Variables para almacenar la selección del usuario
            tipo_barco = tk.StringVar()
            direccion = tk.StringVar()
            
            # Etiqueta y opciones para seleccionar el tipo de barco
            label_mensaje=tk.Label( popup,text=" Debe de ingresar:\n 6 destructores - 4 cruceros - 2 acorazados")
            label_mensaje.pack()
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
                global turno

                seleccion_barco = tipo_barco.get()
                seleccion_direccion = direccion.get()
                if seleccion_barco == "": #Validamos que no hayan datos vacios.
                    label_barco.configure(text="Debe seleccionar un barco:", fg="red")
                elif seleccion_direccion == "":
                    label_direccion.configure(text="Debe seleccionar una dirección:", fg="red")
                else: #Posicionar barco
                    posicionarBarco(seleccion_barco, seleccion_direccion, fila, columna)
                    popup.destroy()


            # Botón para aceptar la selección
            tk.Button(popup, text="Aceptar", command=aceptar).pack()
    elif (columna >= cantColumn and columna <= cantColumn * 2 - 1) and turno == "J2": #Tablero jugador 2
        if len(destructoresJ2) < 6 or len(crucerosJ2) < 4 or len(acorazadosJ2) < 2:
            # Crear una nueva ventana para el pop-up
            popup = tk.Toplevel()
            popup.title("Posicionar barco.")

            # Variables para almacenar la selección del usuario
            tipo_barco = tk.StringVar()
            direccion = tk.StringVar()
            
            # Etiqueta y opciones para seleccionar el tipo de barco
            label_mensaje=tk.Label( popup,text=" Debe de ingresar : \n 6 destructores - 4 cruceros - 2 acorazados")
            label_mensaje.pack()
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
                global turno

                seleccion_barco = tipo_barco.get()
                seleccion_direccion = direccion.get()
                if seleccion_barco == "": #Validamos que no hayan datos vacios.
                    label_barco.configure(text="Debe seleccionar un barco:", fg="red")
                elif seleccion_direccion == "":
                    label_direccion.configure(text="Debe seleccionar una dirección:", fg="red")
                else: #Posicionar barco
                    posicionarBarco(seleccion_barco, seleccion_direccion, fila, columna)
                    popup.destroy()

                    

            # Botón para aceptar la selección
            tk.Button(popup, text="Aceptar", command=aceptar).pack()

def generarTablero(filas, columnas, vtnPrincipal, nkJ1, nkJ2):
    global root, matrizJuego, framePantallaJuego
    global nicknameJ1, nicknameJ2
    global frameJ1, frameJ2
    global cantFilas, cantColumn
    global turno
    global destructoresJ1, crucerosJ1, acorazadosJ1
    global destructoresJ2, crucerosJ2, acorazadosJ2
    
    nicknameJ1 = str(nkJ1)
    nicknameJ2 = str(nkJ2)
    
    
    
    #Ventana principal
    root = vtnPrincipal
    #Frame de la pantalla de juego
    framePantallaJuego = tk.Frame(root, background="black")
    framePantallaJuego.pack(expand=True, fill="both")
    
    # Dividir en 4 columnas
    for col in range(3):
        framePantallaJuego.columnconfigure(col, weight=1)
    # Dividir en 3 filas
    for row in range(2):
        framePantallaJuego.rowconfigure(row, weight=1)
    
    #Matriz para el tablero
    matrizJuego = []
    
    #Cantidad de filas y de columnas del tablero
    cantFilas = filas
    cantColumn = columnas
    
    #Turno de la partida
    turno = "J1"
    
    #Listas de barcos
    destructoresJ1 = []
    crucerosJ1 = []
    acorazadosJ1 = []
    destructoresJ2 = []
    crucerosJ2 = []
    acorazadosJ2 = []
    
    #Cargar imágenes del juego
    imagenes()
    
    frameJ1 = tk.Frame(framePantallaJuego, background="yellow")
    frameJ1.grid(column = 0, columnspan= 3, row = 0, rowspan = 2, sticky="nsew")
    frameJ2 = tk.Frame(framePantallaJuego, background="green")
    
    for fila in range(filas):
        submatrizJuego = [] 

        frameJ1.rowconfigure(fila, weight=1)
        frameJ2.rowconfigure(fila, weight=1)

        for columna in range(columnas * 2):
            if columna < columnas: #Si es el tablero del J1
                frame = frameJ1
            else: #Si es el tablero del J2
                frame = frameJ2
            
            frame.columnconfigure(columna, weight=1)

            celda = tk.Button(frame, command= lambda x=fila, y=columna: onClickCelda(x,y), 
                            text=f"{fila}-{columna}")
            celda.configure(fg="white")
            if columna >= columnas:
                celda.configure(background="red")
            else:
                celda.configure(background="blue")

            celda.grid(row=fila, column=columna, sticky="nsew")
            submatrizJuego.append(celda)

        matrizJuego.append(submatrizJuego)  
        
    messagebox.showinfo("Alerta", "Posicione un barco.")


#TABLERO DE ATAQUE
def cambiarTurnoJuego():
    global turno
    global matrizTableroAtacar
    global frameInfo
    
    if turno == "J1":
        turno = "J2"
        labelAtacante.config(text=nicknameJ2)
        
        #Cambiar contadores de información
        labelCantDestructores.configure(text=str(len(destructoresJ1)))
        labelCantCruceros.configure(text=str(len(crucerosJ1)))
        labelCantAcorazados.configure(text=str(len(acorazadosJ1)))
        
        frameInfo.configure(background="red")
        for fila in matrizTableroAtacar:
            for celda in fila:
                celda.configure(background="blue")
            
    elif turno ==  "J2":
        turno = "J1"
        labelAtacante.config(text=nicknameJ1)
        
        #Cambiar contadores de información
        labelCantDestructores.configure(text=str(len(destructoresJ2)))
        labelCantCruceros.configure(text=str(len(crucerosJ2)))
        labelCantAcorazados.configure(text=str(len(acorazadosJ2)))
        
        frameInfo.configure(background="blue")
        for fila in matrizTableroAtacar:
            for celda in fila:
                celda.configure(background="red")
        
    moverDestructores()  # Llamar a la función para mover destructores en cada turno



def finDelJuego():
    from menuInicial import cargarMenuInicial
    
    messagebox.showinfo("FIN DEL JUEGO", "Gracias por jugar.")
    framePantallaJuego.destroy()
    cargarMenuInicial(root)

def comprobarAtaque(coordenadas):
    global turno
    global destructoresJ1, destructoresJ2
    global crucerosJ1, crucerosJ2
    global acorazadosJ1, acorazadosJ2
    
    jugadorAtacando = turno
    
    if jugadorAtacando == "J2":
        for destructor in destructoresJ1:
            if destructor[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un destructor.")
                destructoresJ1.remove(destructor)
                return
        for crucero in crucerosJ1:
            if crucero[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un crucero.")
                crucerosJ1.remove(crucero)
                return
        for acorazado in acorazadosJ1:
            if acorazado[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un acorazado.")
                acorazadosJ1.remove(acorazado)
                return
        messagebox.showinfo("Alerta", "No ha acertado.")
    elif jugadorAtacando == "J1":
        coordenadas[1] += 20
        for destructor in destructoresJ2:
            if destructor[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un destructor.")
                destructoresJ2.remove(destructor)
                return
        for crucero in crucerosJ2:
            if crucero[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un crucero.")
                crucerosJ2.remove(crucero)
                return
        for acorazado in acorazadosJ2:
            if acorazado[0] == coordenadas:
                messagebox.showwarning("Alerta", "Ha acertado a un acorazado.")
                acorazadosJ2.remove(acorazado)
                return
        messagebox.showerror("Alerta", "No ha acertado.")
        
    #Comprobar si es el fin del juego
    if (len(destructoresJ1) + len(crucerosJ1) + len(acorazadosJ1)) == 0:
        messagebox.showinfo("Fin del juego", "Fin del juego. El jugador 2 ha ganado.")
        finDelJuego()
    elif (len(destructoresJ2) + len(crucerosJ2) + len(acorazadosJ2)) == 0:
        messagebox.showinfo("Fin del juego", "Fin del juego. El jugador 1 ha ganado.")
        finDelJuego()


def onClickCeldaAtacar(fila, columna):
    comprobarAtaque([fila, columna])
    cambiarTurnoJuego()


def generarTableroAtacar():
    global turno
    global frameJ1, frameJ2
    global matrizTableroAtacar, frameTableroAtacar
    global btnVerTablero, btnVolverTablero
    
    frameJ1.grid_forget()
    frameJ2.grid_forget()
    frameTableroAtacar = tk.Frame(framePantallaJuego, background="yellow")
    frameTableroAtacar.grid(column=1, columnspan=3, row=0, rowspan=2, sticky="nsew")
    matrizTableroAtacar = []
    
    for fila in range(cantFilas):
        subMatriz = []
        
        frameTableroAtacar.rowconfigure(fila, weight=1)

        for columna in range(cantColumn):
            frameTableroAtacar.columnconfigure(columna, weight=1)

            celda = tk.Button(frameTableroAtacar, command= lambda f=fila, c=columna: onClickCeldaAtacar(f, c), 
                            text=f"{fila}-{columna}", fg="white")
            if turno == "J1":
                celda.configure(bg="red")
            if turno == "J2":
                celda.configure(bg="blue")

            celda.grid(row=fila, column=columna, sticky="nsew")
            subMatriz.append(celda)
        matrizTableroAtacar.append(subMatriz)


def onClickVerMiTablero():
    global turno
    global frameTableroAtacar, frameJ1, frameJ2, btnVolverTablero, btnVerTablero
    
    
    frameTableroAtacar.grid_forget()
    if turno == "J1":
        frameJ1.grid(column = 1, columnspan= 3, row = 0, rowspan = 2, sticky="nsew")
    if turno == "J2":
        frameJ2.grid(column = 1, columnspan= 3, row = 0, rowspan = 2, sticky="nsew")
    
    btnVerTablero.destroy()
    btnVolverTablero = tk.Button(frameInfo)
    btnVolverTablero.configure(text="Volver al tablero", font=("Arial", 12, "bold"), command=lambda: onClickVolverTablero())
    btnVolverTablero.pack()
    btnVolverTablero.place(x=50, y=800)
    
def onClickVolverTablero():
    global frameTableroAtacar, frameJ1, frameJ2, btnVolverTablero, btnVerTablero
    
    frameJ1.grid_forget()
    frameJ2.grid_forget()
    
    frameTableroAtacar.grid(column=1, columnspan=3, row=0, rowspan=2, sticky="nsew")
    
    btnVolverTablero.destroy()
    btnVerTablero = tk.Button(frameInfo)
    btnVerTablero.configure(text="Ver mi tablero", font=("Arial", 12, "bold"), command=lambda: onClickVerMiTablero())
    btnVerTablero.pack()
    btnVerTablero.place(x=50, y=800)

def guardarPartida():
    with open("partida_guardada.txt", "w") as archivo:
        # Guarda el turno actual
        archivo.write(f"Turno: {turno}\n")
        
        # Guarda la posición de los barcos para J1
        archivo.write("Posicion de barcos para J1:\n")
        for barco in destructoresJ1:
            archivo.write(f"Destructor: {barco}\n")
        for barco in crucerosJ1:
            archivo.write(f"Crucero: {barco}\n")
        for barco in acorazadosJ1:
            archivo.write(f"Acorazado: {barco}\n")
        
        # Guarda la posición de los barcos para J2
        archivo.write("Posicion de barcos para J2:\n")
        for barco in destructoresJ2:
            archivo.write(f"Destructor: {barco}\n")
        for barco in crucerosJ2:
            archivo.write(f"Crucero: {barco}\n")
        for barco in acorazadosJ2:
            archivo.write(f"Acorazado: {barco}\n")
        
        # Agrega más información relevante si es necesario
        
    messagebox.showinfo("Partida Guardada", "La partida ha sido guardada exitosamente.")

def empezarJuego():
    global frameInfo, labelAtacante
    global btnVerTablero, btnVolverTablero
    global nicknameJ1
    global labelCantAcorazados, labelCantDestructores, labelCantCruceros
    
    #Desactivar casillas de posicionamiento de barcos
    for fila in matrizJuego:
        for celda in fila:
            celda.configure(command=None)
    
    #Frame de Información
    frameInfo = tk.Frame(framePantallaJuego, background="blue")
    frameInfo.grid(column=0, row=0, rowspan=2, sticky="nsew")
    
    #Info turno
    labelNombre = tk.Label(frameInfo)
    labelNombre.configure(font=("Arial", 12, "bold"), text="Está atacando: ")
    labelNombre.pack()
    labelNombre.place(x=50, y=50)
    
    labelAtacante = tk.Label(frameInfo)
    labelAtacante.configure(text=nicknameJ1, font=("Arial", 12, "bold"))
    labelAtacante.pack()
    labelAtacante.place(x=50, y=100)
    
    #Frame Datos
    labelBarcosEnemigos = tk.Label(frameInfo)
    labelBarcosEnemigos.configure(font=("Arial", 12, "bold"), text="BARCOS ENEMIGOS")
    labelBarcosEnemigos.pack()
    labelBarcosEnemigos.place(x=50, y=200)
    
    labelDestructores = tk.Label(frameInfo)
    labelDestructores.configure(font=("Arial", 12, "bold"), text="Destructores:")
    labelDestructores.pack()
    labelDestructores.place(x=50, y=250)
    
    labelCantDestructores = tk.Label(frameInfo)
    labelCantDestructores.configure(font=("Arial", 12, "bold"), text="6")
    labelCantDestructores.pack()
    labelCantDestructores.place(x=50, y=300)
    
    labelCruceros = tk.Label(frameInfo)
    labelCruceros.configure(font=("Arial", 12, "bold"), text="Cruceros:")
    labelCruceros.pack()
    labelCruceros.place(x=50, y=350)
    
    labelCantCruceros = tk.Label(frameInfo)
    labelCantCruceros.configure(font=("Arial", 12, "bold"), text="4")
    labelCantCruceros.pack()
    labelCantCruceros.place(x=50, y=400)
    
    labelAcorazados = tk.Label(frameInfo)
    labelAcorazados.configure(font=("Arial", 12, "bold"), text="Acorazados:")
    labelAcorazados.pack()
    labelAcorazados.place(x=50, y=450)
    
    labelCantAcorazados = tk.Label(frameInfo)
    labelCantAcorazados.configure(font=("Arial", 12, "bold"), text="2")
    labelCantAcorazados.pack()
    labelCantAcorazados.place(x=50, y=500)
    
    #Botón para ver tablero
    btnVerTablero = tk.Button(frameInfo)
    btnVerTablero.configure(text="Ver mi tablero", font=("Arial", 12, "bold"), command=onClickVerMiTablero)
    btnVerTablero.pack()
    btnVerTablero.place(x=50, y=750)
    
    #Botón para ver tablero
    btnVerGuardar = tk.Button(frameInfo)
    btnVerGuardar.configure(text="Guardar", font=("Arial", 12, "bold"), command=guardarPartida)
    btnVerGuardar.pack()
    btnVerGuardar.place(x=50, y=900)
    
    generarTableroAtacar()