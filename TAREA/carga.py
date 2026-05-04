import time

# 1. Entrada de datos
tamano = float(input("Ingrese el tamaño del archivo (MB): "))
tiempo_total = float(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {tamano} MB...\n")

# 2. Configuración de la simulación
pasos = 20  # la barra se actualizará 20 veces (de 5% en 5%)
intervalo = tiempo_total / pasos

# 3. Simulación de la barra de progreso
for i in range(pasos + 1):
    porcentaje = int((i / pasos) * 100)
    
    # Construir barra
    llenos = int(i)
    vacios = pasos - llenos
    barra = "[" + "#" * llenos + "-" * vacios + "]"
    
    # Mostrar barra en la misma línea
    print(f"\r{barra} {porcentaje}%", end="")
    
    time.sleep(intervalo)

# 4. Mensaje final
print(f"\n\n¡Archivo de {tamano} MB subido con éxito!")