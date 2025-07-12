# Funcion para leer la matriz
def leer_matriz(filas, columnas):
    print("Ingrese los valores: ")
    matriz = [ ]
    for i in range(filas):
        fila = [ ]
        for j in range(columnas):
            valor = float(input(f"Valor en [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Funcion para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Funcion que suma los elementos de la columna escogida
def sumar_columna(matriz, columna):
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma

if __name__ == "__main__":
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = leer_matriz(filas, columnas)
    mostrar_matriz(matriz)

    # Pide la columna que se quiere sumar
    while True:
        col = int(input(f"Ingrese el número de la columna que desea sumar (0 a {columnas - 1}): "))
        if 0 <= col < columnas:
            break
        else:
            print("Columna invalida. Vuelve a intentar.")

    resultado = sumar_columna(matriz, col)
    print(f"La suma de los elementos de la columna {col} es: {resultado}")