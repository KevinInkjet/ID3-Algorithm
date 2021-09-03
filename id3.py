archivo = open("C:/Users/Owner/Documents/LCC/Machine Learning/ID3-Algorithm/prueba.txt") # Abrir un archivo

total_lines = sum(1 for line in archivo)
print("Líneas del archivo: ", total_lines) #Para conseguir la cantidad de líneas del archivo
archivo.close()

archivo = open("C:/Users/Owner/Documents/LCC/Machine Learning/ID3-Algorithm/prueba.txt") # Abrir un archivo

datos = []
for lineas in archivo:
    datos.append(lineas.split())

print(datos)

print(len(datos[2])) #Con len() obtenemos la longitud de una línea, en este caso la línea 3

palabra = "hola,"
print(palabra)
palabra = palabra.replace(",", '') #Quitamos las comas
print(palabra)