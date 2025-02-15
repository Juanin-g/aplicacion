import streamlit as st
import pandas as pd
import matplotlib.pyplot as pyplot
#leer datos
titanic = pd.read_csv("titanic.csv")
 # Crear un gráfico con Plotly (por ejemplo, un gráfico de barras de la edad)
fig = px.histogram(titanic, x="Age")

# Configuración de la página
st.set_page_config(page_title="Dashboars", layout="wide")
st.sidebar.title("Analisis de datos")

# Pestañas
tab1, tab2 = st.tabs(["Cuadros de desglose", "Graficas"])
with tab1:
  st.header("informaciòn general")
  st.plotly_chart(titanic.head())
  st.plotly_chart(titanic.info())

with tab2:


# Mostrar el gráfico en Streamlit
  st.plotly_chart(fig)
