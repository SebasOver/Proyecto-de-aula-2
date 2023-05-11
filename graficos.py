import matplotlib.pyplot as plt

def generar_grafico(x, y):
    plt.plot(x, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Corriente')
    plt.title('Gráfico de Corriente en función del Tiempo')
    plt.show()
