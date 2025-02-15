import streamlit as st
import pandas as pd
import pyplot
#leer datos
titanic = pd.read_csv("titanic.csv")

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
  st.pyplot(fig)(titanic.plot(subplots= True, figsize=(15, 12), sharex= False, sharey=False))

