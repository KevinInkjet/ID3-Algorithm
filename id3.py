archivo = open("C:/Users/Owner/Documents/LCC/Machine Learning/ID3-Algorithm/prueba.txt")

linea = archivo.readline()
while linea != '':
    print(linea)
    linea = archivo.readline()

archivo.close()

archivo = open("C:/Users/Owner/Documents/LCC/Machine Learning/ID3-Algorithm/prueba.txt")

linea = archivo.read()
while linea != '':
    print(linea)
    linea = archivo.read()

archivo.close()