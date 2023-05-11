def calcular_corriente(voltaje, resistencia):
    corriente = voltaje / resistencia
    return corriente

def calcular_resistencia_equivalente_en_serie(resistencias):
    resistencia_total = sum(resistencias)
    return resistencia_total

def calcular_resistencia_equivalente_en_paralelo(resistencias):
    resistencia_total = 1 / sum(1 / resistancia for resistancia in resistencias)
    return resistencia_total

def calcular_potencia(voltaje, resistencia):
    potencia = (voltaje ** 2) / resistencia
    return potencia

def calcular_voltaje(corriente, resistencia):
    voltaje = corriente * resistencia
    return voltaje
