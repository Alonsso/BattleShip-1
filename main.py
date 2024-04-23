import tkinter as tk
from menuInicial import cargarMenuInicial

def main():
    # Ventana principal
    root = tk.Tk()
    root.title('BattleShip')

    # Obtener las dimensiones de la pantalla
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()

    # Establecer el tamaño de la ventana para que coincida con las dimensiones de la pantalla
    root.geometry(f"{ancho}x{alto}")
    root.resizable(True, True)
    root.configure(background="red")

    # Cargar menú inicial
    cargarMenuInicial(root)

    # Mantener ventana abierta
    root.mainloop()

main()
