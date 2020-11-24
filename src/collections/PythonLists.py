'''
@author: finfantefran
'''

# Declaracion
lista = [1, 2, 3, 4, 5]
print(lista)

# Acceso a valores
print(lista[:2], lista[0])

# Suma de listas
lista2 = lista + [1, 2, 3, 4, 5]

# Anhadir valores a la lista
lista2.append(2)

# Ver tamanho
len(lista)

# Asiganar valores de lista a variables, debe coincidir el tamanho con el num de variables
x, y, z, w, k = lista
print(x, y)

line = ['a', 10, 10, (2020, 10, 31)]
x1, x2, x3, date1 = line

""" Ordenar y revertir orden, operaciones"""

a = [4, 1, 5, 2]

# Revierte en el orden actuallos valores
a.reverse()
a[::-1]
print(a)

# Ordena de mayor a menor, reverse: True/False
a.sort(reverse=True)
print(a)

# Operaciones sobre una lista

lista1 = ['a', 'list', 'of', 'words']
lista2 = [s.upper() for s in lista1]
print(lista2)

# Operaciones matematicas sobre listas

x = [3, 1, 4, 2]
min1 = min(x)
max1 = max(x)
print(min1, max1)

""" Listas y operaciones filter"""

# filtrar una lista que devuelva los valores que cumplen cierta condicion
mylist = [1, -2, 3, -5, 6, -7, 8]
pos = [n for n in mylist if n > 0]
print(pos)

mylist = [1, -2, 3, -5, 6, -7, 8]
positiveList = [n if n > 0 else 0 for n in mylist]
print(positiveList)

""" Ordenar listas de Strings"""
list1 = ['b', 'AA', 'bbb', 'ZZZ', 'CCC']
# se ordenan en cuestion al valor decimal de cada caracrer
print(sorted(list1, key=len))
print(sorted(list1, key=str.lower))

""" Expresioones en listas"""
nums = [1, 2, 3, 4]
cubes = [n * n * n for n in nums]
print(cubes)





