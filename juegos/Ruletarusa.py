'''
reto de programacion simulador de probabilidad llamada ruleta rusa

1. descripciom de problemas
se requiere desarrollar un programa en Phyton que simule un sistema de arcade basado en un revolver de 6 camara. 
el programa debe gestionar eventos aleatorios, pausas de ejecucion para mejorar la experiencia de usuario y control del flujo basado en condiciones
de victpria o derrota.


2. requerimientos tecnicos:
El algotitmo debe cumplir los siguientes requisitos:

- inicializacion definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6.
- bucle de juego: el usuario debe interactuar manualmente para girar el tambor y disparar.
- mecanica de azar: en cada turno, la posiscion de la recamara que queda al frente en el percutor debe ser aleatorio simulando el giro del tambor
- condicion de derrota: si la recamara seleccionada coincide con la de la bala, el programa termina inmediatamente.
- condicion de victoria: el jugador gana si logra sobrevivir a 5 intentos (ya que el sexto intento deberia ser fatal)
'''

import random, time
print ("bienvenido al simulador de ruleta rusa")
print ("="*50) 

input("poner Bala en el tambor (precionar enter)")
bala = random.randint (1,6)
time.sleep(0.5)

disparos = 0 #variable para contar los disparos realizar

while True: 
    input ("girar el tambor (precionar enter)")
    recamara = random.randint(1, 6)

    input ("apuntar y disparar (precionar enter)")
    time.sleep (1)

    if recamara == bala:
        print ("¡BANG! haz perdido. La bala estaba en la recamara"  "numero", bala)
        
        
    else:
        
        disparos += 1 
        print("haz sobrevivido a este intento.")
        print("intento de disparos:", disparos)

        if disparos == 5:
            print("felicidades haz ganado al sobrevivir a 5 intentos.)")
            break

print ("="*50)
print ("fin del juego - gracias por jugar")
print ("="*50)