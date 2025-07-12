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
    print("Matriz ingresada:")
    for fila in matriz:
        print(fila)

# Funcion que suma los elementos de una fila escogida
def sumar_fila(matriz, fila_num):
    return sum(matriz[fila_num])

if __name__ == "__main__":
    #Pide el nunero de filas y columnas
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))

    matriz = leer_matriz(filas, columnas)
    mostrar_matriz(matriz)

    # Se valida la fila
    while True:
        fila = int(input(f"Ingrese el numero de la fila que desea sumar (0 a {filas - 1}): "))
        if 0 <= fila < filas:
            break
        else:
            print("Fila invalida. Vuelve a intentar.")

    resultado = sumar_fila(matriz, fila)
    print(f"La suma de los elementos de la fila {fila} es: {resultado}")