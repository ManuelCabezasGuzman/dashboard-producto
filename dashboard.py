import streamlit as st
import pandas as pd

st.title("📊 Dashboard de prueba")
st.write("Este es tu primer dashboard en Python usando Streamlit 🚀")

# Dataset de ejemplo
df = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo'],
    'Ventas': [1500, 2300, 1800]
})

st.bar_chart(df.set_index('Mes'))
