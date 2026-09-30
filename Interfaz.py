import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Lumina", page_icon="🧵")

st.title("Calculadora de Precios Lumina 🧵")
st.markdown("---")

# Entrada del precio base
precio_lista = st.number_input("Ingresá el Precio de Lista:", min_value=0.0, step=100.0, format="%.2f")

# Selector de opciones basado en tu Excel
opcion = st.selectbox("Seleccioná el Canal / Cantidad de Cuotas:", [
    "6 Cuotas (Divisores 1.20)", 
    "9 Cuotas (Divisores 1.30)", 
    "18 Cuotas (Divisores 1.45)",
    "6 Cuotas (GK9, GK26, PRO) (Divisores 1.20)", 
    "9 Cuotas (GK9, GK26, PRO) (Divisores 1.30)",
    "6 CUOTAS (WEB LUMINA) (Divisores 1.25)",
    "6 CUOTAS PRO (WEB LUMINA) (Divisores 1.25)",
    "TRANSFERENCIA (WEB LUMINA) (Divisores 1.20)"
    
])

# Diccionario con la lógica de fondo (coeficientes de la imagen)
configuracion = {
    "6 Cuotas (Divisores 1.20)": (1.20),
    "9 Cuotas (Divisores 1.30)": (1.30),
    "18 Cuotas (Divisores 1.45)": (1.45),
    "6 Cuotas (GK9, GK26, PRO) (Divisores 1.20): ": (1.20),
    "9 Cuotas (GK9, GK26, PRO) (Divisores 1.30)": (1.30),
    "6 CUOTAS (WEB LUMINA) (Divisores 1.25)": (1.25),
    "6 CUOTAS PRO (WEB LUMINA) (Divisores 1.25)": (1.25),
    "TRANSFERENCIA (WEB LUMINA) (Divisores 1.10)": (1.10)
}

# Realizar el cálculo automáticamente
div_cuota = configuracion[opcion]

if precio_lista > 0:
    # La misma cuenta que hacés en el Excel
    resultado = (precio_lista / div_cuota)
    
    st.markdown("### Resultado Neto:")
    st.success(f"## $ {resultado:,.2f}")
    
    # Detalle técnico opcional
    with st.expander("Ver detalle de la cuenta"):
        st.write(f"Precio: {precio_lista} / Coeficiente Cuota: {div_cuota} / Coeficiente Impuesto: {div_imp}")
else:
    st.info("Ingresá un precio mayor a cero para ver el resultado.")

st.markdown("---")

st.caption("Herramienta desarrollada para gestión de Mercado Libre y Lumina Web.")



