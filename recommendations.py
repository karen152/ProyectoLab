def generar_recomendaciones(entradas, diagnostico):
    """
    Genera recomendaciones basadas en las entradas del usuario y el diagnóstico.
    :param entradas: Diccionario con los datos biométricos del usuario.
    :param diagnostico: Resultado del diagnóstico (0 a 1).
    :return: Lista de recomendaciones.
    """
    recomendaciones = []

    # Evaluar la temperatura
    if entradas["temperatura"] >= 39:
        recomendaciones.append("Consulta a un médico urgentemente. Tu temperatura es muy alta.")
    elif entradas["temperatura"] >= 37.5:
        recomendaciones.append("Descansa e hidrátate. Controla tu temperatura regularmente.")

    # Evaluar la frecuencia cardíaca
    if entradas["frecuencia_cardiaca"] > 100:
        recomendaciones.append("Podrías estar experimentando taquicardia. Considera buscar ayuda médica.")
    elif entradas["frecuencia_cardiaca"] < 60:
        recomendaciones.append("Tu frecuencia cardíaca es baja. Consulta a un médico si te sientes débil.")

    # Evaluar la presión arterial
    if entradas["presion_arterial"] > 140:
        recomendaciones.append("Tu presión arterial es alta. Reduce el consumo de sal y consulta a un médico.")
    elif entradas["presion_arterial"] < 90:
        recomendaciones.append("Tu presión arterial es baja. Asegúrate de estar hidratado y alimentado.")

    # Evaluar el nivel de oxígeno
    if entradas["nivel_oxigeno"] < 95:
        recomendaciones.append("El nivel de oxígeno en sangre es bajo. Considera buscar atención médica.")

    # Recomendaciones según el diagnóstico
    if diagnostico >= 0.7:
        recomendaciones.append("Alta probabilidad de infección. Busca atención médica pronto.")
    elif diagnostico >= 0.4:
        recomendaciones.append("Observa tus síntomas y consulta a un médico si empeoran.")
    else:
        recomendaciones.append("Estás estable. Mantén un estilo de vida saludable.")

    return recomendaciones