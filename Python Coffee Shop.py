import time

# CREADO POR MI 

#1  SIN PARAMETROS Y SIN RETORNO

def mostrar_bienvenida():

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║               ☕ PYTHON COFFEE SHOP  ☕                  ║
║                                                          ║
║            Sistema Inteligente de Pedidos                ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                       MENÚ PRINCIPAL                     ║
║                                                          ║
║     ┌────────────────────────────────────────────┐       ║
║     │                                            │       ║
║     │   [ P ]  Café Pequeño            $ 2.00    │       ║
║     │   [ M ]  Café Mediano    ☕☕    $ 3.00    │       ║
║     │   [ G ]  Café Grande     ☕☕    $ 4.00    │       ║
║     │                                            │       ║
║     └────────────────────────────────────────────┘       ║
║                                                          ║
║              ✨ Calidad • Aroma • Energía ✨             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")



#2 SIN PARAMETROS Y CON RETORNO     

def elegir_tamaño():
    tamaño = input ("¿Qué tamaño desea? (P/M/G): ").upper()
    return tamaño


#3 CON PARAMETROS Y CON RETORNO  

def calcular_precio(letra_tamaño):

    if letra_tamaño == "P":
        precio = 2.0
    elif letra_tamaño == "M":
        precio = 3.0
    elif letra_tamaño == "G":
        precio = 4.0
    else:
        print("Tamaño no válido")
        return 0

    impuesto = precio * 0.10
    total = precio + impuesto
    return total


#4 CON PARAMETROS SIN RETORNO   

def preparar_pedido(letra_tamaño, total):

    if letra_tamaño == "P":
        nombre = "Pequeño"

    elif letra_tamaño == "M":
        nombre = "Mediano"

    elif letra_tamaño == "G":
        nombre = "Grande"

    else:
        nombre = "Desconocido"

    print("\n☕ Preparando su café", nombre)
    time.sleep(1)

    barra = [
        "█░░░░░░░░░ 10%",
        "███░░░░░░░ 30%",
        "█████░░░░░ 50%",
        "███████░░░ 70%",
        "█████████░ 90%",
        "██████████ 100%"
    ]

    for progreso in barra:
        print(progreso)
        time.sleep(0.6)
    print(f"💵 El total fue: ${total:.2f}")
    print("✅ ¡Disfrute su bebida!")


mostrar_bienvenida()

tamaño_usuario = elegir_tamaño()
precio_final = calcular_precio(tamaño_usuario)

if precio_final > 0:
    preparar_pedido(tamaño_usuario, precio_final)

    


    


   