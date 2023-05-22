import calculos
import graficos

def mostrar_menu():
    print("Simulador de Flujo Eléctrico")
    print("1. Calcular corriente eléctrica")
    print("2. Calcular resistencia equivalente en serie")
    print("3. Calcular resistencia equivalente en paralelo")
    print("4. Calcular potencia disipada")
    print("5. Calcular voltaje")
    print("6. Generar gráfico de corriente en función del tiempo")
    print("7. Salir")

def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("¡Error! Ingrese un valor numérico válido.")

def calcular_corriente():
    print(">> Calcular corriente eléctrica")
    voltaje = obtener_float("Ingrese el valor del voltaje (V): ")
    resistencia = obtener_float("Ingrese el valor de la resistencia (Ω): ")
    corriente = calculos.calcular_corriente(voltaje, resistencia)
    print(f"La corriente eléctrica es: {corriente:.2f} A")

def calcular_resistencia_equivalente_en_serie():
    print(">> Calcular resistencia equivalente en serie")
    num_resistencias = int(input("Ingrese el número de resistencias en el circuito: "))
    resistencias = []
    for i in range(num_resistencias):
        resistencia = obtener_float(f"Ingrese el valor de la resistencia {i+1} (Ω): ")
        resistencias.append(resistencia)
    resistencia_equivalente_serie = calculos.calcular_resistencia_equivalente_en_serie(resistencias)
    print(f"La resistencia equivalente en serie es: {resistencia_equivalente_serie:.2f} Ω")

def calcular_resistencia_equivalente_en_paralelo():
    print(">> Calcular resistencia equivalente en paralelo")
    num_resistencias = int(input("Ingrese el número de resistencias en el circuito: "))
    resistencias = []
    for i in range(num_resistencias):
        resistencia = obtener_float(f"Ingrese el valor de la resistencia {i+1} (Ω): ")
        resistencias.append(resistencia)
    resistencia_equivalente_paralelo = calculos.calcular_resistencia_equivalente_en_paralelo(resistencias)
    print(f"La resistencia equivalente en paralelo es: {resistencia_equivalente_paralelo:.2f} Ω")

def calcular_potencia_disipada():
    print(">> Calcular potencia disipada")
    voltaje = obtener_float("Ingrese el valor del voltaje (V): ")
    resistencia = obtener_float("Ingrese el valor de la corriente (A): ")
    potencia = calculos.calcular_potencia(voltaje, resistencia)
    print(f"La potencia disipada es: {potencia:.2f} W")

def calcular_voltaje():
    print(">> Calcular voltaje")
    corriente = obtener_float("Ingrese el valor de la corriente (A): ")
    resistencia = obtener_float("Ingrese el valor de la resistencia (Ω): ")
    voltaje = calculos.calcular_voltaje(corriente, resistencia)
    print(f"El voltaje es: {voltaje:.2f} V")

def generar_grafico_corriente_tiempo():
    print(">> Generar gráfico de corriente en función del tiempo")
    num_puntos = int(input("Ingrese el número de puntos para el gráfico: "))
    tiempos = []
    corrientes = []
    for i in range(num_puntos):
        tiempo = obtener_float(f"Ingrese el valor del tiempo {i+1}: ")
        corriente = obtener_float(f"Ingrese el valor de la corriente {i+1}: ")
        tiempos.append(tiempo)
        corrientes.append(corriente)
    try:
        graficos.generar_grafico(tiempos, corrientes)

        # Análisis de pendiente
        if len(tiempos) >= 2:
            pendiente = (corrientes[-1] - corrientes[0]) / (tiempos[-1] - tiempos[0])
            if pendiente > 0:
                significado_pendiente = "La corriente está aumentando con el tiempo."
            elif pendiente < 0:
                significado_pendiente = "La corriente está disminuyendo con el tiempo."
            else:
                significado_pendiente = "La corriente se mantiene constante en el tiempo."

            print(f"Significado de la pendiente: {significado_pendiente}")
        else:
            print("¡Error! Se requieren al menos 2 puntos para calcular la pendiente.")
    except ZeroDivisionError:
        print("¡Error! La división por cero no está permitida.")

def ejecutar_opcion(opcion):
    if opcion == "1":
        calcular_corriente()
    elif opcion == "2":
        calcular_resistencia_equivalente_en_serie()
    elif opcion == "3":
        calcular_resistencia_equivalente_en_paralelo()
    elif opcion == "4":
        calcular_potencia_disipada()
    elif opcion == "5":
        calcular_voltaje()
    elif opcion == "6":
        generar_grafico_corriente_tiempo()
    elif opcion == "7":
        print("¡Hasta luego!")
        return False
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        continuar = ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
