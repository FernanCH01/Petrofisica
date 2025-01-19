# Import Python Libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from pathlib import Path
import lasio
import welly



#icono
icon = Image.open('logo/icono.jpg')

st.set_page_config(page_title="Petrophysics App", page_icon=icon)
# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
footer {
  display: none;
}
</style>""",
    unsafe_allow_html=True,
)

# Insert title for app
st.title("Petrophysics App")

st.write("---")

logo = Image.open("logo/logo_stech.jpg")
st.image(logo, width=100, use_container_width=True)


# Add information of the app
st.markdown(
    """
  
Petrophysics App es una solución integral enfocada en la gestión y análisis de datos de pozos petroleros. Proporciona herramientas especializadas para evaluar registros eléctricos, sónicos, de densidad y porosidad, permitiendo una caracterización precisa de los yacimientos y la identificación eficiente de áreas con potencial productivo."""

)

# Add additional information
expander = st.expander("Information")
expander.write(
    "Petrophysics App es una aplicación web de código abierto, desarrollada completamente en Python, diseñada para analizar y optimizar datos de registros de pozos. Facilita la interpretación de parámetros petrofísicos como porosidad, saturación de fluidos y permeabilidad, apoyando la toma de decisiones en tiempo real y la caracterización de yacimientos."
)

# Insert subheader
st.subheader("*¿Qué son los registros de pozos?*")

st.markdown(
    """

Los registros de pozos son mediciones obtenidas con herramientas especiales dentro de un pozo perforado. Estas registran propiedades físicas como resistividad, densidad, porosidad y velocidad sónica, ayudando a analizar las características del subsuelo y los yacimientos."""

)

# Sección para importar y explorar archivos LAS
st.subheader("Importar y explorar archivos LAS")

# Cargar archivo LAS
uploaded_file = st.file_uploader("Cargar archivo LAS", type=["las"])

if uploaded_file is not None:
    try:
        # Convertir archivo cargado a formato compatible con lasio
        las = lasio.read(uploaded_file.read().decode("utf-8"))

        # Mostrar metadatos
        st.write("### Metadatos del archivo LAS")
        st.write("Campo: Volve (Noruega)")
        st.text(f"Versión: {las.version[0].value}")
        st.text(f"Pozo: {las.well.WELL.value}")

        # Mostrar canales disponibles
        st.write("### Canales disponibles")
        st.text(", ".join(las.keys()))

        # Convertir datos del archivo LAS a DataFrame
        las_df = las.df()

        # Mostrar DataFrame
        st.write("### Vista previa de los datos")
        st.dataframe(las_df.head(10))

        # Agregar descarga del DataFrame en formato CSV
        csv = las_df.to_csv().encode('utf-8')
        st.download_button(
            label="Descargar datos como CSV",
            data=csv,
            file_name="datos_volve.csv",
            mime="text/csv",
        )
    except Exception as e:
        st.error(f"Error al procesar el archivo LAS: {e}")
else:
    st.info("Por favor, sube un archivo LAS para explorar los datos.")
