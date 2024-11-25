import streamlit as st
from utils import YEAR_MIN, YEAR_MAX
from controller_data import controller_data

# Instancia del controlador
controlador = controller_data()

# src/filtrado.py

import streamlit as st
from utils import YEAR_MIN, YEAR_MAX

def filtrado_informacion(controller_data, controlador):
    """Página para filtrar datos por rango de años."""
    st.header("Filtrado de Información")
    st.write("Selecciona el rango de años para filtrar los datos.")

    # Barra de rango de años
    selected_years = st.slider(
        "Selecciona el rango de años",
        min_value=YEAR_MIN,
        max_value=YEAR_MAX,
        value=(YEAR_MIN, YEAR_MAX)
    )

    lista_de_anos = [range(selected_years[0], selected_years[1] + 1)]
    keyword = st.text_input("Ingresa una palabra clave para filtrar por programa académico:")


    # Filtrar archivos por años usando el controller
    archivos_filtrados = controller_data.filtrar_datos(controlador, lista_de_anos,keyword )

    if archivos_filtrados:
        st.write("Archivos filtrados:")
        st.write(archivos_filtrados)
    else:
        st.warning("No hay archivos disponibles para el rango de años seleccionado.")