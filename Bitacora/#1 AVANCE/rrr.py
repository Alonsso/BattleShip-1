filas = 5
columnas = 5
num_barcos = 3

def crear_tablero(num_filas, num_columnas):
    tablero = []
    for _ in range(num_filas):
        fila_vacia = [' '] * num_columnas
        tablero.append(fila_vacia)
    return tablero

def imprimir_tablero(tablero):
    print("   ", end="")
    for i in range(len(tablero[0])):
        print(f"{i} ", end="")
    print() 

    for i, fila in enumerate(tablero):
        print(f"{i}  {' | '.join(fila)} {' |'}")

def colocar_barcos(tablero, num_barcos):
    barcos = 0
    while barcos < num_barcos:
        fila = int(input("Indicar el número de fila para el barco: "))
        columna = int(input("Indicar el número de columna para el barco: "))
        
        if fila >= len(tablero) or columna >= len(tablero[0]):
            print("Posición inválida. Fuera de los límites del tablero.")
        elif tablero[fila][columna] == 'D':
            print("Esta posición ya fue utilizada.")
        else:
            tablero[fila][columna] = 'D'
            barcos += 1

def reacomodar_barcos(tablero, num_barcos):
    print("Reacomodando los barcos:")
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 'D':
                tablero[i][j] = ' '  
    
    colocar_barcos(tablero, num_barcos)

tablero = crear_tablero(filas, columnas)

colocar_barcos(tablero, num_barcos)

print("Posición de los barcos:")
imprimir_tablero(tablero)

continuar = input("Si desea reacomodarlos inserte '1', si no inserte '2': ")

if continuar == '1':
    reacomodar_barcos(tablero, num_barcos)
    print("Nueva posición de los barcos:")
    imprimir_tablero(tablero)
elif continuar == '2':
    print("No se reacomodarán los barcos.")
else:
    print("Opción no válida. No se reacomodarán los barcos.")

