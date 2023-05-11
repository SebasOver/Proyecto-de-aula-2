import calculos
import graficos

def menu():
    print("Bienvenido")
    print("1. Calcular corriente eléctrica")
    print("2. Calcular resistencia equivalente en serie")
    print("3. Calcular resistencia equivalente en paralelo")
    print("4. Calcular potencia disipada")
    print("5. Calcular voltaje")
    print("6. Generar gráfico de corriente en función del tiempo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        voltaje = float(input("Ingrese el valor del voltaje (V): "))
        resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))
        corriente = calculos.calcular_corriente(voltaje, resistencia)
        print("La corriente eléctrica es:", corriente, "A")
    elif opcion == "2":
        num_resistencias = int(input("Ingrese el número de resistencias en el circuito: "))
        resistencias = []
        for i in range(num_resistencias):
            resistencia = float(input("Ingrese el valor de la resistencia {} (Ω): ".format(i + 1)))
            resistencias.append(resistencia)
        resistencia_equivalente_serie = calculos.calcular_resistencia_equivalente_en_serie(resistencias)
        print("La resistencia equivalente en serie es:", resistencia_equivalente_serie, "Ω")
    elif opcion == "3":
        num_resistencias = int(input("Ingrese el número de resistencias en el circuito: "))
        resistencias = []
        for i in range(num_resistencias):
            resistencia = float(input("Ingrese el valor de la resistencia {} (Ω): ".format(i + 1)))
            resistencias.append(resistencia)
        resistencia_equivalente_paralelo = calculos.calcular_resistencia_equivalente_en_paralelo(resistencias)
        print("La resistencia equivalente en paralelo es:", resistencia_equivalente_paralelo, "Ω")
    elif opcion == "4":
        voltaje = float(input("Ingrese el valor del voltaje (V): "))
        resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))
        potencia = calculos.calcular_potencia(voltaje, resistencia)
        print("La potencia disipada es:", potencia, "W")
    elif opcion == "5":
        corriente = float(input("Ingrese el valor de la corriente (A): "))
        resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))
        voltaje = calculos.calcular_voltaje(corriente, resistencia)
        print("El voltaje es:", voltaje, "V")
    elif opcion == "6":
        x = [1, 2, 3, 4, 5]  # Ejemplo de datos para el eje x (tiempo)
        y = [10, 20, 30, 40, 50]  # Ejemplo de datos para el eje y (corriente)
        graficos.generar_grafico(x, y)
    elif opcion == "7":
        print("¡Hasta luego!")
        return
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    menu()

if __name__ == "__main__":
    menu()
