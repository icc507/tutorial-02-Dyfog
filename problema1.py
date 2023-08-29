#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#20 90 hola
#mundo 44
#La salida debe ser
#('mundo', 44, 20, 90, 'hola', 'mundo', 44)
entrada1 = input().split()
entrada2 = input().split()

t1 = []
for item in entrada1:
    if item.isdigit():
        t1.append(int(item))
        continue
    if item.isdecimal():
        t1.append(float(item))
        continue
    else:
        t1.append(item)

t2 = []
for item in entrada2:
    if item.isdigit():
        t2.append(int(item))
        continue
    if item.isdecimal():
        t2.append(float(item))
        continue
    else:
        t2.append(item)

salida = t2 + t1 + t2
print(salida)
