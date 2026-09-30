def calcular_precio():
    # Definimos los coeficientes según la imagen
    # Estructura: 'Nombre': (divisor_cuotas)
    configuracion = {
        "6": (1.20),
        "9": (1.30),
        "18": (1.45),
        "6 (GK9, GK26, PRO)": (1.20),
        "9 (GK9, GK26, PRO)": (1.30),
        "6 CUOTAS (WEB LUMINA)": (1.25),
        "6 CUOTAS PRO (WEB LUMINA)": (1.25),
        "TRANSFERENCIA (WEB LUMINA)": (1.10)
    }

    print("--- Calculadora de Precios Lumina ---")
    precio_lista = float(input("Ingrese el precio de lista: "))
    
    print("Opciones de cuotas: ", list(configuracion.keys()))
    opcion = input("Seleccione una opción: ")

    if opcion in configuracion:
        div_cuota = configuracion[opcion]
        # Realizamos la cuenta de fondo
        resultado = (precio_lista / div_cuota)
        print(f"\nResultado final: {resultado:.2f}")
    else:
        print("Opción no válida.")


calcular_precio()

