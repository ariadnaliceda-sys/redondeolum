def calcular_precio():
    # Definimos los coeficientes según la imagen
    # Estructura: 'Nombre': (divisor_cuotas, divisor_impuesto)
    configuracion = {
        "1": (1.21, 1.0), # El 1.0 es porque en la imagen de 1 cuota solo divide por 1.21
        "6": (1.35, 1.21),
        "9": (1.58, 1.21),
        "1 (GK9, GK26, PRO)": (1.105, 1.0),
        "6 (GK9, GK26, PRO)": (1.35, 1.105),
        "9 (GK9, GK26, PRO)": (1.58, 1.105),
        "6 CUOTAS (WEB LUMINA)": (1.39, 1.21),
        "TRANSFERENCIA (WEB LUMINA)": (1.112, 1.21)
    }

    print("--- Calculadora de Precios Lumina ---")
    precio_lista = float(input("Ingrese el precio de lista: "))
    
    print("Opciones de cuotas: ", list(configuracion.keys()))
    opcion = input("Seleccione una opción: ")

    if opcion in configuracion:
        div_cuota, div_imp = configuracion[opcion]
        # Realizamos la cuenta de fondo
        resultado = (precio_lista / div_cuota) / div_imp
        print(f"\nResultado final: {resultado:.2f}")
    else:
        print("Opción no válida.")


calcular_precio()

