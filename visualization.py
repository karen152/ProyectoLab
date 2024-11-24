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

# import matplotlib.pyplot as plt

# def mostrar_graficos(entradas):
#     fig, axs = plt.subplots(3, 1, figsize=(8, 10))

#     axs[0].plot([entradas['temperatura']], 'ro-', label="Temperatura")
#     axs[0].set_title("Temperatura")
#     axs[0].legend()

#     axs[1].plot([entradas['frecuencia_cardiaca']], 'go-', label="Frecuencia Cardíaca")
#     axs[1].set_title("Frecuencia Cardíaca")
#     axs[1].legend()

#     axs[2].plot([entradas['presion_arterial']], 'bo-', label="Presión Arterial")
#     axs[2].set_title("Presión Arterial")
#     axs[2].legend()

#     plt.tight_layout()
#     plt.show()


