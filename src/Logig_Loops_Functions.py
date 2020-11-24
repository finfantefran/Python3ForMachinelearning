'''
@author: finfantefran
'''

"""Orden de prioridad operadores"""
order = '^ */ +-'

""" FOR LOOPS"""
x = ['a', 'b', 'c']
for z in x:
    print(z)

for z in reversed(x):
    print(z)
    
for z in range(len(x)):
    print(x[z])
    
# si se incluye un tratamiento de exception en el for, este se sigue ejecutando
line = '1 2 3 4 10e abc'
suma1 = 0
invalidStr = ""
print('String of numbers:', line)
for str1 in line.split(" "):
    try:
        suma1 = suma1 + eval(str1)
    except:
        invalidStr = invalidStr + str1 + ' '
        print(str1)

"""EXPONENTES en python"""

# **
# pow(2,4) elvear 2 a 4

"""BUCLES ANIDADOS"""
iterations = 8
for x in range(1, iterations + 1):  # en rango de 1 a 8+1
    z = ""
    for y in range(1, x + 1):  # en rango de 1 a x+1
        z = z + str(y)
    print(z)
    
"""split(), convertir en una lista una cadena de palabras  por ejemplo, separadas por espacios, comas..."""

x = 'hola me llamo Fran'
x2 = x.split(" ")
print(x2)

for z in x.split(" "):
    print(z)

wordCount = 0
str1 = 'this is a string with a set of words in it'
# print('Left-justified strings:')
# print('-----------------------')
# for w in str1.split():
#     print('%-10s' % w) # anhade 10 espacios a la derech de un string  
#     if(wordCount % 2 == 0):
#         print("")
#     wordCount = wordCount + 1
# print("\n")

print('Right-justified strings:')
print('------------------------')
wordCount = 0
for w in str1.split():
    print('%10s' % w, end='')  # anhade 10 espacios a la izquierda de un string
    wordCount = wordCount + 1
    if(wordCount % 2 == 0):
        print("")

"""join(), junta palabras separadas concatenandolas con el caracter que se le aplique """

"""WHILE LOOPS"""
x = 0
while x < 5:
    print(x)
    x += 1
    
lista = [1, 2, 3, 4]
while lista:  # bucle while sobre una lista, para borrar elementos
    print(lista)
    print(lista.pop())  # borra el ultimo elemento

"""LOGICA CONDICIONAL"""

if x < 0:
    pass
elif x > 5:
    pass
elif x == 25:
    pass
else:
    print("else")

""" break, continue, pass STATEMENTS"""

# break: salir de un loop
# continue: continnua con la siguiente iteracion o valor del bucle, un else por ejemplo
# pass: no hacer nada

"""COMPARISION BOOLEANS # in/not in/is/is not"""

# in y not, para saber si existe un valor en una secuencia
# is y is not, para comprobar si dos variables son el mismo objeto

""" and, or, not"""
    
""" LOCAL AND GLOBAL VARIABLES """ 
# LOCALES
# :: parametro de funcion
# :: pertenece a un bucle

# global z si le asignas un valor dentro de una función, este no permanece fuera de esta
# nonlocal p

""" PASSING BY REFERENCE VS VALUE"""
# En el paso por referencia los cambios que se le hacen a la variable pasada la modifican tambien fuera.
# Referencia:: listas, diccionarios, conjuntos.
# Valor:: Enteros, flotantes, cadenas, lógicos.

"""Especificar valores por defecto en la funcion"""
# Se pueden dejar valores por defecto, por si no quieres dar ningun valor al llamar a la funcion


def numberFunc(a, b=10):
    print (a, b)


numberFunc(2)

""" Devolver multiples valores"""


def MultipleValues():
    return 'a', 'b', 'c'  


print(MultipleValues())

""" Funcion que recibe multiples valores"""

  
def suma(*values):
    sum1 = 0
    for x in values:
        sum1 = sum1 + x
    return sum1


print(suma(1, 2, 3, 4))

""" LAMBDA EXPRESSIONS """ 
add = lambda x, y: x + y
print(add(1, 2))

