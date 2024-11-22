
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función para generar la doble hélice
def generar_helice_adn(secuencia_adn):
    # Definir los colores para cada base del ADN
    colores = {'A': 'blue', 'T': 'red', 'C': 'green', 'G': 'yellow'}

    # Número de pasos o puntos por vuelta de la hélice
    pasos_por_vuelta = 10
    vueltas = len(secuencia_adn) // pasos_por_vuelta  # Determinar cuántas vueltas completas tiene la secuencia

    # Generar coordenadas en 3D para la doble hélice
    t = np.linspace(0, 4 * np.pi, len(secuencia_adn))  # Usamos 4 pi para 2 vueltas completas
    x = np.sin(t)  # Coordenada X (variación sinusoidal)
    y = np.cos(t)  # Coordenada Y (variación cosenoidal)
    z = np.linspace(0, 1, len(secuencia_adn))  # Coordenada Z (posición en la hélice)

    # Preparar la visualización
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Dibuja los puntos de la hélice para cada base
    for i, base in enumerate(secuencia_adn):
        ax.scatter(x[i], y[i], z[i], color=colores[base], s=100, label=base if i == 0 else "")

    # Dibuja las conexiones entre las dos cadenas (bases complementarias)
    for i in range(0, len(secuencia_adn) - 1, 2):
        # Conectar las bases emparejadas (A-T, C-G)
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color='black', lw=1)

    # Personalizar la visualización
    ax.set_title("Representación 3D de la Doble Hélice de ADN")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(False)

    # Ajustes de la vista
    ax.view_init(30, 60)  # Ajusta el ángulo de visualización
    plt.legend()

    # Mostrar la visualización
    plt.show()

# Secuencia de ADN para ilustrar
secuencia_adn = input("Introduce la secuencia de ADN del animal: ")

# Generar y visualizar la doble hélice del ADN
generar_helice_adn(secuencia_adn)

from Bio import SeqIO
import matplotlib.pyplot as plt

# Función para obtener los codones de una secuencia de ADN
def obtener_codones(secuencia_adn):
    return [secuencia_adn[i:i+3] for i in range(0, len(secuencia_adn), 3)]

# Función para graficar los codones
def graficar_codones(codones):
    # Contar la frecuencia de cada codón
    from collections import Counter
    frecuencia_codones = Counter(codones)

    # Ordenar por frecuencia
    codones, frecuencias = zip(*sorted(frecuencia_codones.items()))

    # Graficar las frecuencias de codones
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(codones, frecuencias, color='purple')

    ax.set_title('Frecuencia de Codones')
    ax.set_xlabel('Codón')
    ax.set_ylabel('Frecuencia')
    plt.xticks(rotation=90)  # Rotar las etiquetas de los codones
    plt.show()

# Ingresar una secuencia de ADN (por ejemplo, de un animal)
secuencia_adn = input("Introduce la secuencia de ADN del animal: ")

# Obtener los codones
codones = obtener_codones(secuencia_adn)

# Graficar los codones
graficar_codones(codones)

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Función para crear un modelo de la doble hélice del ADN
def ilustrar_doble_helice(secuencia_adn):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Parametrización de la doble hélice
    num_pasos = len(secuencia_adn) // 2  # Para simplificar
    angulo = np.linspace(0, 4 * np.pi, num_pasos)  # Ángulo para crear la hélice
    x = np.sin(angulo)  # Movimiento en X (para crear espiral)
    y = np.cos(angulo)  # Movimiento en Y (para crear espiral)
    z = np.linspace(0, 1, num_pasos)  # Eje Z: desplazamiento vertical

    # Dibujar la primera cadena
    ax.plot(x, y, z, color='b', label='Cadena 1 (A, T, G, C)')

    # Dibujar la segunda cadena, desplazada
    ax.plot(x, -y, z, color='r', label='Cadena 2 (A, T, G, C)')

    # Etiquetas y título
    ax.set_title("Estructura Secundaria del ADN (Doble Hélice)")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")

    # Mostrar la gráfica
    ax.legend()
    plt.show()

# Entrada de la secuencia de ADN
secuencia_adn = input("Introduce la secuencia de ADN: ")

# Ilustrar la doble hélice del ADN
ilustrar_doble_helice(secuencia_adn)

from Bio.Seq import Seq
import matplotlib.pyplot as plt

# Función para calcular la proporción de nucleótidos
def calcular_proporcion_nucleotidos(secuencia_adn):
    # Convertir la secuencia de ADN en un objeto Seq
    secuencia = Seq(secuencia_adn)

    # Contar la frecuencia de cada nucleótido
    count_a = secuencia.count('A')  # Adenina
    count_t = secuencia.count('T')  # Timina
    count_c = secuencia.count('C')  # Citosina
    count_g = secuencia.count('G')  # Guanina

    # Total de nucleótidos en la secuencia
    total_nucleotidos = len(secuencia)

    # Calcular la proporción de cada nucleótido
    proporcion_a = count_a / total_nucleotidos
    proporcion_t = count_t / total_nucleotidos
    proporcion_c = count_c / total_nucleotidos
    proporcion_g = count_g / total_nucleotidos

    # Visualización en gráfico de pastel
    nucleotidos = ['Adenina (A)', 'Timina (T)', 'Citosina (C)', 'Guanina (G)']
    proporciones = [proporcion_a, proporcion_t, proporcion_c, proporcion_g]
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Colores para cada nucleótido

    # Crear el gráfico de pastel
    plt.figure(figsize=(8, 8))
    plt.pie(proporciones, labels=nucleotidos, autopct='%1.1f%%', startangle=140, colors=colores)
    plt.title("Proporción de Nucleótidos en la Secuencia de ADN")
    plt.show()

# Entrada de la secuencia de ADN
secuencia_adn = input("Introduce la secuencia de ADN: ")

# Calcular y mostrar la proporción de nucleótidos
calcular_proporcion_nucleotidos(secuencia_adn)
#ia_adn)
