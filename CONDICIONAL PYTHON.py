 

# esto es un comentario de una sola linea 
"""es
to es 
un comentario de multiples lineas en }
Python
"""
# Condicionales 

"""
simples  si()   | if():
Dobles   si() si() sino()  | if(): elif():
Multiples   switch         | no existe 

"""

# Phyton trabaje con IF simple 
"""
Palabrasreservada  (Condicion)
SentenciaUno
SentenciaDos

"""
if (True):
    print("hola")
    print("Como estas")

if (False   ):
    print("bien")
    print("y usted")


a=5
b=3

if (a>b):
    print ("A es mayor que B")
#comparacion de numeros boleanos en python 
C = False

if (C== True):
    print ("C es VERDADERO")
#
    caracter = 'a'
    if(caracter == 'b'):
        print ("el caracter es:", caracter)

palabra = "hola"
if (palabra=="chao"):
    print("la palabra es:", caracter)


 #python trabake con el si doble 
"""
 palabrasreservada  (Condicion)
SentenciaUno
SentenciaDos

SINO(Condicion)
SentenciaUno
SentenciaDos
 """

nota = 1

if (nota >= 4):
    print("excelente")
elif (nota >= 2 and nota <= 3):
    print ("necesitas recuperar")
elif ( nota >= 1 and nota<2):
    print ("porque no se pasa a administracion")
else: #condicion de cierre
         print ("su nota fue cero")