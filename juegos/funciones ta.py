import random 


# 1 /funciones que no reciben parametros devuelven resultados

def mostrar_bienvenida ():
    
    # No hay parametros de entrada entre los parentesis.

    print ("bienvenido a la funcion de bienvenida")
    print (" por favor, selecciona una opcion del menu.")
    print ("1. Opcion 1")
     print ("2. Opcion 2")
     print ("3. Opcion 3")
     print ("4. salir ")
    
    # para usar la funcion simplemente la llamamos por su nombre seguido de parentesis 
    mostrar_bienvenida()

    # 2. FUNCION QUE RECIBE PARAMETROS PERO NO DEVUELVE RESULTADOS 

    def saludar_persona(nombre, edad):
       
       # recibe nombre y edad y lo da como parametros de entrada 

       print ("hola {nombre}, veo que tienes {edad} años! ")

       #no tiene return, solo imprime en pantalla el mensaje 

       saludar_persona ("Estrella", 45) # llamamos la funcion con argumentos especificos. 

       # 3. FUNCIONES QUE NO DEVUELVEN PARAMETROS PERO DEVUELVEN UN RESULTADO 

       def tirar_dato()
          
        # NO RECIBE PARAMETROS DE ENTRADA 
        
        numero_obtenido = random.randint (1,6) #GENERA NUMERO ALEATORIO ENTRE 1 Y  6

        return numero_obtenido        # DEVUELVE EL NUMERO OBTENIDO 
       
       resultado = tirar_dato() # LLAMAMOS A LA FUNCION Y ALMACENAMOS RESULTADO EN UN VARIABLE.
       print (f "haz tirado el dado obtuviste: {resultado}") # recibimos resultados

       def calcular_area_rectngulo (base, altura):
         
         area = base * altura 
         return area
       
       mi_area = calcular_area_rectngulo (5, 10)

       print (f" el area del rectangulo es: {mi_area}")



