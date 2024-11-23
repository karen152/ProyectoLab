import matplotlib.pyplot as plt

def mostrar_historial(datos):
    """
    Genera gráficos del historial de datos biométricos.
    :param datos: Diccionario con listas de datos históricos.
    """
    if not datos:
        print("No hay historial disponible para mostrar.")
        return

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()  # Convierte la matriz de ejes en una lista para iterar fácilmente

    # Gráfico de temperatura
    axs[0].plot(datos["temperatura"], marker='o', label="Temperatura (°C)")
    axs[0].set_title("Evolución de la Temperatura")
    axs[0].set_xlabel("Sesión")
    axs[0].set_ylabel("Temperatura (°C)")
    axs[0].legend()

    # Gráfico de frecuencia cardíaca
    axs[1].plot(datos["frecuencia_cardiaca"], marker='o', color='green', label="Frecuencia Cardíaca (bpm)")
    axs[1].set_title("Evolución de la Frecuencia Cardíaca")
    axs[1].set_xlabel("Sesión")
    axs[1].set_ylabel("Frecuencia Cardíaca (bpm)")
    axs[1].legend()

    # Gráfico de presión arterial
    axs[2].plot(datos["presion_arterial"], marker='o', color='red', label="Presión Arterial (mmHg)")
    axs[2].set_title("Evolución de la Presión Arterial")
    axs[2].set_xlabel("Sesión")
    axs[2].set_ylabel("Presión Arterial (mmHg)")
    axs[2].legend()

    # Gráfico de diagnóstico
    axs[3].plot(datos["diagnostico"], marker='o', color='purple', label="Diagnóstico")
    axs[3].set_title("Evolución del Diagnóstico")
    axs[3].set_xlabel("Sesión")
    axs[3].set_ylabel("Diagnóstico")
    axs[3].legend()

    plt.tight_layout()
    plt.show()