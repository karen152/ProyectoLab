import matplotlib.pyplot as plt

def mostrar_graficos(entradas):
    from fuzzy_logic import SistemaDifuso

    sistema = SistemaDifuso()
    fig, axs = plt.subplots(4, 1, figsize=(8, 10))

    sistema.temperatura.view(ax=axs[0])
    axs[0].axvline(entradas['temperatura'], color='red', linestyle='--', label=f'Temperatura: {entradas["temperatura"]}')
    axs[0].legend()

    sistema.frecuencia_cardiaca.view(ax=axs[1])
    axs[1].axvline(entradas['frecuencia_cardiaca'], color='red', linestyle='--', label=f'Frecuencia: {entradas["frecuencia_cardiaca"]}')
    axs[1].legend()

    sistema.presion_arterial.view(ax=axs[2])
    axs[2].axvline(entradas['presion_arterial'], color='red', linestyle='--', label=f'Presión: {entradas["presion_arterial"]}')
    axs[2].legend()

    sistema.nivel_oxigeno.view(ax=axs[3])
    axs[3].axvline(entradas['nivel_oxigeno'], color='red', linestyle='--', label=f'Oxígeno: {entradas["nivel_oxigeno"]}')
    axs[3].legend()

    plt.tight_layout()
    plt.show()