# Funcion para hacer la matriz
def leer_matriz(filas, columnas, nombre):
    print(f"Ingrese los valores {nombre}:")
    matriz = [ ]
    for i in range(filas):
        fila = [ ]
        for j in range(columnas):
            n = float(input(f"Valor en [{i}][{j}]: "))
            fila.append(n)
        matriz.append(fila)
    return matriz

# Función que muestra la matriz
def mostrar_matriz(matriz):
    print("Resultado:")
    for fila in matriz:
        print(fila)

# Función para sumar las matrices
def sumar_matrices(m1, m2):
    resultado = [ ]
    for i in range(len(m1)):
        fila = [ ]
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

# Función para restar las matrices
def restar_matrices(m1, m2):
    resultado = [ ]
    for i in range(len(m1)):
        fila = [ ]
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

if __name__ == "__main__":
    # Aca se ingresan las filas y las columnas
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))
    #Se crean dos matrices
    matriz1 = leer_matriz(filas, columnas, "A")
    matriz2 = leer_matriz(filas, columnas, "B")
    #Aca se pide si es suma o resta
    print("Que operacion deseas realizar")
    print("1. Suma")
    print("2. Resta")
    opcion = input("Escribe 1 o 2: ")
    #En esta parte se valida la opcion
    if opcion == "1":
        resultado = sumar_matrices(matriz1, matriz2)
    elif opcion == "2":
        resultado = restar_matrices(matriz1, matriz2)
    else:
        print("Opcion invalida")
        exit()

    mostrar_matriz(resultado)