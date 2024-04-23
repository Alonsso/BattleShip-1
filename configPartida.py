import tkinter as tk
from tkinter import messagebox
from juego import generarTablero




# Función que se ejecuta al hacer clic en el botón "Jugar"
def onClickBtnJugar(root):
    global cantColumn, cantFilas, entryJugador1, entryJugador2, entryFila, entryColumna

    # Inicializar nombres de jugadores
    nickNameJ1 = entryJugador1.get()
    nickNameJ2 = entryJugador2.get()

    # Verificar que los nicknames sean diferentes
    if nickNameJ1 != nickNameJ2:
        # Verificar que el número de filas sea mayor o igual a 10
        if int(entryFila.get()) >= 10:
            cantFilas = int(entryFila.get())
            
            # Verificar que el número de columnas sea mayor o igual a 20
            if int(entryColumna.get()) >= 20:
                cantColumn = int(entryColumna.get())
                # Cambiar al frame de juego
                frameConfig.pack_forget()
                generarTablero(cantFilas, cantColumn, root, nickNameJ1, nickNameJ2)
            else:
                messagebox.showinfo("Alerta", "¡Debe tener 20 columnas o más!")
        else:
            messagebox.showinfo("Alerta", "¡Debe tener 10 filas o más!")
    else:
        messagebox.showinfo("Alerta", "¡Los nicknames deben ser diferentes!")

# Función para cargar la configuración de la partida
def cargarConfigPartida(root):
    global frameConfig, entryJugador1, entryJugador2, entryFila, entryColumna

    # Frame CONFIGURACIONES
    frameConfig = tk.Frame(root)
  
    frameConfig.configure(background="light blue")
    frameConfig.pack(expand=True, fill="both")

    # Entry JUGADOR 1
    # Label
    labelJugador1 = tk.Label(frameConfig)
    labelJugador1.configure(
        text="NICKNAME JUGADOR 1",
        width=100,
    )
    labelJugador1.pack()
    labelJugador1.place(x=280, y=150, height=100)

    # Entry
    entryJugador1 = tk.Entry(frameConfig)
    entryJugador1.configure(
        width=100
    )
    entryJugador1.pack()
    entryJugador1.place(x=330, y=280, height=100)

    # Entry JUGADOR 2
    # Label
    labelJugador2 = tk.Label(frameConfig)
    labelJugador2.configure(
        text="NICKNAME JUGADOR 2",
        width=100,
    )
    labelJugador2.pack()
    labelJugador2.place(x=1100, y=150, height=100)

    # Entry
    entryJugador2 = tk.Entry(frameConfig)
    entryJugador2.configure(
        width=100,
    )
    entryJugador2.pack()
    entryJugador2.place(x=1150, y=280, height=100)

    # Cantidad filas/columnas
    # Label FILA
    labelFila = tk.Label(frameConfig)
    labelFila.configure(
        text="Ingrese la cantidad de filas:",
        width=80
    )
    labelFila.pack()
    labelFila.place(x=350, y=410, height=80)

    # Entry FILA
    entryFila = tk.Entry(frameConfig)
    entryFila.configure(
        width=60
    )
    entryFila.pack()
    entryFila.place(x=450, y=520, height=60)

    # Label COLUMNA
    labelColumna = tk.Label(frameConfig)
    labelColumna.configure(
        text="Ingrese la cantidad de columnas:",
        width=80
    )
    labelColumna.pack()
    labelColumna.place(x=1170, y=410, height=80)

    # Entry COLUMNA
    entryColumna = tk.Entry(frameConfig)
    entryColumna.configure(
        width=60
    )
    entryColumna.pack()
    entryColumna.place(x=1270, y=520, height=60)

    # Botón Jugar
    btnJugar = tk.Button(frameConfig)
    btnJugar.configure(
        text="JUGAR",
        command=lambda: onClickBtnJugar(root),
        width=120
    )
    btnJugar.pack()
    btnJugar.place(x=600, y=650, height=120)
