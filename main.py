def registrar_temperaturas_semanales():
    """
    Permite ingresar las temperaturas diarias de 7 días consecutivos,
    calcula y muestra estadísticas, y alerta sobre temperaturas extremas.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese las temperaturas diarias de los últimos 7 días:")
    for dia in dias:
        while True:
            try:
                temperatura = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para la temperatura.")

    # 1. Mostrar la temperatura máxima y el día en que ocurrió.
    max_temperatura = max(temperaturas)
    indice_max = temperaturas.index(max_temperatura)
    dia_max = dias[indice_max]
    print(f"\nTemperatura máxima: {max_temperatura}°C ({dia_max})")

    # 2. Mostrar la temperatura mínima y el día en que ocurrió.
    min_temperatura = min(temperaturas)
    indice_min = temperaturas.index(min_temperatura)
    dia_min = dias[indice_min]
    print(f"Temperatura mínima: {min_temperatura}°C ({dia_min})")

    # 3. Calcular y mostrar el promedio semanal.
    promedio_semanal = sum(temperaturas) / len(temperaturas)
    print(f"Promedio semanal: {promedio_semanal:.2f}°C")

    # 4. Mostrar qué días estuvieron por encima del promedio.
    dias_sobre_promedio = []
    for i in range(len(temperaturas)):
        if temperaturas[i] > promedio_semanal:
            dias_sobre_promedio.append(dias[i])

    if dias_sobre_promedio:
        print("Días con temperatura por encima del promedio:", ", ".join(dias_sobre_promedio))
    else:
        print("Ningún día tuvo una temperatura por encima del promedio.")

    # 5. Si alguna temperatura supera los 40°C o está por debajo de 0°C, mostrar una alerta.
    alerta_extrema = False
    for i in range(len(temperaturas)):
        if temperaturas[i] > 40:
            print(f"\n¡ALERTA! Temperatura extrema alta ({temperaturas[i]}°C) el día {dias[i]}.")
            alerta_extrema = True
        elif temperaturas[i] < 0:
            print(f"\n¡ALERTA! Temperatura extrema baja ({temperaturas[i]}°C) el día {dias[i]}.")
            alerta_extrema = True

    if not alerta_extrema:
        print("\nNo se registraron temperaturas extremas.")

# Ejecutar el programa
if __name__ == "__main__":
    registrar_temperaturas_semanales()