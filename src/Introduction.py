'''
@author: finfantefran
'''

"""Multiline statements"""
total = 1 + \
        2 + \
        3
print(total)

"""Multiple statements in one line"""
a = 10;b = 11;c = 12;

'word'
"Sentence."
"""Paragraph, more than one line."""
# comment line

"""Literal character"""
a1 = r'\n'; print(a1)
a2 = '\''; print(a2)

"""Cuando se llama a un modulo en python directamente, la variable __name__ vale __main_
    de otra forma, tendra el valor del nombre de la clase a la que pertenece."""
if __name__ == '__main__':
    print(__name__)

"""Num bases"""
x = 14
print('Binario: ', bin(x));print('Octal: ', oct(x));print('Hexadecimal: ', hex(x))

print('Binario: ', format(x, 'b')); print('Octal: ', format(x, 'o'));print('Hexadecimal: ', format(x, 'x'))

"""chr() convierte integer a character"""
x = chr(65); print(x)
result = ""

for x in range(ord('A'), ord('Z')):
    print(x, chr(x))
    result = result + chr(x) + ' '
print("result: ", result) 

"""round() redondeo de decimales, al mas cercano siempre, mayor o menor"""
print(round(1.2545, 1))  # (num, num decimales)

"""Formateo de numeros """
x = 1.45363534

print(format(x, '0.2f'))  # num, num decimales en float

print('value is {:0.3f}'.format(x))  # {formateo para el valor x}

from decimal import Decimal
a = Decimal('4.2'); print(a)

"""Fracciones"""

from fractions import Fraction

a = Fraction(5, 3);b = Fraction(7, 16); print(a + b)
a.numerator; a.denominator  # numerador y denominador
print(format(float(a + b), '0.2f'))  # covirtiendo a float la fraccion y formatting

""" Unicode, UTF-8"""
c = u'Hola que tal';print(c)

chinese1 = u'\u5c07\u63a2\u8a0e HTML5 \u53ca\u5176\
u4ed6'
hiragana = u'D3 \u306F \u304B\u3063\u3053\u3043\u3043 \
u3067\u3059!'
print('Chinese:', chinese1)
print('Hiragana:', hiragana)

"""Formatting Strings > 3.6 """
import string
# string.lstring(), string.rstring(), and string.center() for positioning a text string

""" Variables no utilizadas, None"""
# Se distinguen en python
# None indica "no value"
# Se puede implenentar None en comparaciones logicas

"""Comprobar si un string contiene digits o characters"""
str1 = "a"
if(str1.isdigit()):
    print("is a digit: ", str1)

"""Buscar y sustituir string en otro string"""
s1 = 'abc'
s2 = 'ABC'
text = 'Este texto contiene abc'

pos1 = text.find(s1);print(pos1)
print('a' in s1)  # Para saber la presencia de un elemento 

text = text.replace('abc', 'was'); print(text)  # reemplazar

"""Eliminar caracteres al principio, final, y ambos"""
text = "  hola que ase  "
print('x', text.rstrip(), 'y');print('x', text.lstrip(), 'y'); print('x', text.strip(), 'y')

"""Substituir espacios"""
import re
text = 'a     b'
a = text.replace(' ', '')
b = re.sub('\s+', ' ', text) # misma funcion que replace, substituye el caracter especial space por ' '
print(a)
print(b)


"""Trabajando con DATATIME"""
import time
import datetime

print("Time in seconds since the epoch: %s" %time.time())
x1=time.time()
print("Current date and time: " , datetime.datetime.
now())
print("Or like this: " ,datetime.datetime.now().
strftime("%y-%m-%d-%H-%M"))
print("Current year: ", datetime.date.today().
strftime("%Y"))
print("Month of year: ", datetime.date.today().
strftime("%B"))
print("Week number of the year: ", datetime.date.
today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().
strftime("%w"))
print("Day of year: ", datetime.date.today().
strftime("%j"))
print("Day of the month : ", datetime.date.today().
strftime("%d"))
print("Day of week: ", datetime.date.today().
strftime("%A"))
x2=time.time()-x1
print(x2)


from datetime import timedelta # PAra realizar operaciones con tipos datetime
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b; print(c.total_seconds()/3600)


"""Convertir String to date"""
from datetime import datetime
text='2014-08-13'
y=datetime.strptime(text,'%Y-%m-%d');print(type(y))



"""Command-Line Arguments"""
import sys
print('Program name: ',sys.argv[0])



