import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Lumina", page_icon="🧵")

st.title("Calculadora de Precios Lumina 🧵")
st.markdown("---")

# Entrada del precio base
precio_lista = st.number_input("Ingresá el Precio de Lista:", min_value=0.0, step=100.0, format="%.2f")

# Selector de opciones basado en tu Excel
opcion = st.selectbox("Seleccioná el Canal / Cantidad de Cuotas:", [
    "1 Cuota (Divisor 1.21)", 
    "6 Cuotas (Divisores 1.35 / 1.21)", 
    "9 Cuotas (Divisores 1.58 / 1.21)", 
    "1 Cuota (GK9, GK26, PRO) (Divisor 1.105)", 
    "6 Cuotas (GK9, GK26, PRO) (Divisores 1.35 / 1.105)", 
    "9 Cuotas (GK9, GK26, PRO) (Divisores 1.58 / 1.105)",
    "6 CUOTAS (WEB LUMINA) (Divisores 1.39 / 1.21)",
    "6 CUOTAS PRO (WEB LUMINA) (Divisores 1.39 / 1.105)",
    "TRANSFERENCIA (WEB LUMINA) (Divisores 1.112 / 1.21)"
])

# Diccionario con la lógica de fondo (coeficientes de la imagen)
configuracion = {
    "1 Cuota (Divisor 1.21)": (1.21, 1.0),
    "6 Cuotas (Divisores 1.35 / 1.21)": (1.35, 1.21),
    "9 Cuotas (Divisores 1.58 / 1.21)": (1.58, 1.21),
    "1 Cuota (GK9, GK26, PRO) (Divisor 1.105)": (1.105, 1.0),
    "6 Cuotas (GK9, GK26, PRO) (Divisores 1.35 / 1.105)": (1.35, 1.105),
    "9 Cuotas (GK9, GK26, PRO) (Divisores 1.58 / 1.105)": (1.58, 1.105),
    "6 CUOTAS (WEB LUMINA) (Divisores 1.39 / 1.21)": (1.39, 1.21),
    "6 CUOTAS PRO (WEB LUMINA) (Divisores 1.39 / 1.105)": (1.39, 1.105),
    "TRANSFERENCIA (WEB LUMINA) (Divisores 1.112 / 1.21)": (1.112, 1.21)
}

# Realizar el cálculo automáticamente
div_cuota, div_imp = configuracion[opcion]

if precio_lista > 0:
    # La misma cuenta que hacés en el Excel
    resultado = (precio_lista / div_cuota) / div_imp
    
    st.markdown("### Resultado Neto:")
    st.success(f"## $ {resultado:,.2f}")
    
    # Detalle técnico opcional
    with st.expander("Ver detalle de la cuenta"):
        st.write(f"Precio: {precio_lista} / Coeficiente Cuota: {div_cuota} / Coeficiente Impuesto: {div_imp}")
else:
    st.info("Ingresá un precio mayor a cero para ver el resultado.")

st.markdown("---")

st.caption("Herramienta desarrollada para gestión de Mercado Libre y Lumina Web.")



