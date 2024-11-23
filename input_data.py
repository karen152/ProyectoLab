# def obtener_datos_usuario():
#     """
#     Recoge los datos básicos del usuario: síntomas y variables biométricas.
#     Retorna un diccionario con los datos.
#     """
#     print("Por favor, ingrese los siguientes datos biométricos:")
#     try:
#         temperatura = float(input("Temperatura corporal (°C): ").strip())
#         frecuencia_cardiaca = float(input("Frecuencia cardíaca (bpm): ").strip())
#         presion_arterial = float(input("Presión arterial sistólica (mmHg): ").strip())
#         nivel_oxigeno = float(input("Nivel de oxígeno en sangre (%): ").strip())

#         return {
#             "temperatura": temperatura,
#             "frecuencia_cardiaca": frecuencia_cardiaca,
#             "presion_arterial": presion_arterial,
#             "nivel_oxigeno": nivel_oxigeno
#         }

#     except ValueError as e:
#         print(f"Error: Entrada inválida. Detalles: {e}")
#         return None

def obtener_datos_usuario():
    """
    Recoge los datos básicos del usuario: síntomas y variables biométricas.
    Retorna un diccionario con los datos.
    """
    print("Por favor, ingrese los siguientes datos biométricos:")

    try:
        temperatura = float(input("Temperatura corporal (°C, rango 35-42): ").strip())
        if not 35 <= temperatura <= 42:
            raise ValueError("La temperatura debe estar entre 35°C y 42°C.")

        frecuencia_cardiaca = float(input("Frecuencia cardíaca (bpm, rango 50-130): ").strip())
        if not 50 <= frecuencia_cardiaca <= 130:
            raise ValueError("La frecuencia cardíaca debe estar entre 50 bpm y 130 bpm.")

        presion_arterial = float(input("Presión arterial sistólica (mmHg, rango 80-180): ").strip())
        if not 80 <= presion_arterial <= 180:
            raise ValueError("La presión arterial debe estar entre 80 mmHg y 180 mmHg.")

        nivel_oxigeno = float(input("Nivel de oxígeno en sangre (%), rango 90-100): ").strip())
        if not 90 <= nivel_oxigeno <= 100:
            raise ValueError("El nivel de oxígeno en sangre debe estar entre 90% y 100%.")

        return {
            "temperatura": temperatura,
            "frecuencia_cardiaca": frecuencia_cardiaca,
            "presion_arterial": presion_arterial,
            "nivel_oxigeno": nivel_oxigeno
        }

    except ValueError as e:
        print(f"Error: {e}")
        return None