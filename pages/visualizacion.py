import streamlit as st
from pages.utils import cargar_datos

def visualizacion_datos(carpeta):
    """Página para visualizar datos cargados."""
    st.header("Visualización de Datos")

    # Mostrar todos los datos cargados
    datos = cargar_datos(carpeta)
    if not datos.empty:
        st.write("Datos cargados:")
        st.dataframe(datos)
    else:
        st.warning("No hay datos disponibles. Regresa a la pestaña de carga para cargar datos.")
