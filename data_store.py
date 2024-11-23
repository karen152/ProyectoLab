import json
import os

HISTORIAL_FILE = "historial_diagnosticos.json"

def guardar_diagnostico(datos, resultado):
    entrada = {
        "temperatura": datos["temperatura"],
        "frecuencia_cardiaca": datos["frecuencia_cardiaca"],
        "presion_arterial": datos["presion_arterial"],
        "nivel_oxigeno": datos["nivel_oxigeno"],
        "diagnostico": resultado,
        # "fecha": "2024-11-22"  # Ejemplo, podrías agregar la fecha real aquí
    }

    try:
        # Cargar historial existente o crear uno nuevo
        if os.path.exists(HISTORIAL_FILE):
            with open(HISTORIAL_FILE, "r") as file:
                historial = json.load(file)
        else:
            historial = []

        # Agregar la nueva entrada
        historial.append(entrada)

        # Guardar el historial actualizado
        with open(HISTORIAL_FILE, "w") as file:
            json.dump(historial, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el diagnóstico: {e}")


def cargar_historial():
    """
    Carga y devuelve el historial de diagnósticos.
    """
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r") as file:
            return json.load(file)
    else:
        return []



def cargar_datos_para_graficos():
    """
    Carga los datos del historial desde el archivo JSON para generar gráficos.
    :return: Lista de datos del historial o una lista vacía.
    """
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: El archivo de historial no contiene un JSON válido.")
                return []
    else:
        print("Advertencia: El archivo de historial no existe.")
        return []

import json

def cargar_datos_historial():
    try:
        with open("historial_diagnosticos.json", "r") as archivo:
            historial = json.load(archivo)
        # Transforma los datos en el formato adecuado
        datos = {
            "temperatura": [item["temperatura"] for item in historial],
            "frecuencia_cardiaca": [item["frecuencia_cardiaca"] for item in historial],
            "presion_arterial": [item["presion_arterial"] for item in historial],
            "diagnostico": [item["diagnostico"] for item in historial],
        }
        return datos
    except FileNotFoundError:
        print("El archivo historial_diagnosticos.json no se encontró.")
        return {}
    except KeyError as e:
        print(f"Error en la estructura del historial: falta la clave {e}")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}
    except Exception as e:
        print(f"Error inesperado: {e}")
        return {}

