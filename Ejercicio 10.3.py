# Funcion para leer la matriz
def leer_matriz(filas, columnas):
    print("Ingrese los valores: ")
    matriz = [ ]
    for i in range(filas):
        fila = [ ]
        for j in range(columnas):
            n = float(input(f"Valor en [{i}][{j}]: "))
            fila.append(n)
        matriz.append(fila)
    return matriz

# Funcion para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Funcion para transponer una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [ ]
    for j in range(columnas):
        nueva_fila = [ ]
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

if __name__ == "__main__":
    # Se pide valores para el tamaño de la matriz
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))

    matriz = leer_matriz(filas, columnas)

    # Muestra la matriz original
    print("Matriz original:")
    mostrar_matriz(matriz)

    # Se transpone la matriz
    transpuesta = transponer_matriz(matriz)

    # Muestra la matriz transpuesta
    print("Matriz transpuesta:")
    mostrar_matriz(transpuesta)