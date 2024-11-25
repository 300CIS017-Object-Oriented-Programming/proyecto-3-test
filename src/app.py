import streamlit as st
import carga, filtrado, visualizacion
from controller_data import controller_data


# Carpeta de trabajo
CARPETA = "docs/temp"

def main():
    controlador = controller_data()
    # Pestañas principales
    tabs = st.tabs(["Carga de Información", "Filtrado", "Visualización"])

    # Pestaña: Carga de Información
    with tabs[0]:
        carga.cargar_informacion(CARPETA)

    # Pestaña: Filtrado
    with tabs[1]:
        filtrado.filtrado_informacion(controller_data)

    # Pestaña: Visualización
    with tabs[2]:
        visualizacion.visualizacion_datos(CARPETA)

if __name__ == "__main__":
    main()
