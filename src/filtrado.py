
import streamlit as st
from utils import YEAR_MIN, YEAR_MAX
from controller_data import controller_data

# Instancia del controlador
controlador = controller_data()

def filtrado_informacion(carpeta):
    """Página para filtrar datos por rango de años y palabra clave."""
    st.header("Filtrado de Información")
    st.write("Selecciona el rango de años para filtrar los datos.")

    # Barra de rango de años
    selected_years = st.slider(
        "Selecciona el rango de años",
        min_value=YEAR_MIN,
        max_value=YEAR_MAX,
        value=(YEAR_MIN, YEAR_MAX)
    )

    # Input para la palabra clave
    keyword = st.text_input("Ingresa una palabra clave para filtrar por programa académico:")

    if keyword:
        # Filtrar datos usando el controller
        controlador.filtrar_datos(range(selected_years[0], selected_years[1] + 1), keyword)
        filtered_data = controlador._controller_data__data_frame_filtrado

        if not filtered_data.empty:
            st.write("Datos filtrados:")
            st.dataframe(filtered_data)
        else:
            st.warning("No hay datos disponibles para el rango de años y palabra clave seleccionados.")
    else:
        st.warning("Por favor, ingresa una palabra clave para filtrar los datos.")