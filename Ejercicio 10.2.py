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

# Función para multiplicar las matrices
def multiplicar_matrices(m1, m2):
    resultado = [ ]
    for i in range(len(m1)):
        fila = [ ]
        for j in range(len(m1[0])):
            fila.append(m1[i][j] * m2[i][j])
        resultado.append(fila)
    return resultado

if __name__ == "__main__":
    # Aca se ingresan las filas y las columnas
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))
    #Se crean dos matrices
    matriz1 = leer_matriz(filas, columnas, "A")
    matriz2 = leer_matriz(filas, columnas, "B")
    resultado = multiplicar_matrices(matriz1,matriz2)
mostrar_matriz(resultado)