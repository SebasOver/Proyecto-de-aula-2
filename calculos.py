def calcular_corriente(voltaje, resistencia):
    corriente = voltaje / resistencia
    return corriente

def calcular_resistencia_equivalente_en_serie(resistencias):
    resistencia_total = sum(resistencias)
    return resistencia_total

def calcular_resistencia_equivalente_en_paralelo(resistencias):
    resistencia_total = 1 / sum(1 / resistancia for resistancia in resistencias)
    return resistencia_total

def calcular_potencia(voltaje, corriente):
    potencia = voltaje * corriente
    return potencia

def calcular_voltaje(corriente, resistencia):
    voltaje = corriente * resistencia
    return voltaje

def calcular_resistencia_ley_ohm(voltaje, corriente):
    resistencia = voltaje / corriente
    return resistencia
