import streamlit as st
from pages import carga, filtrado, visualizacion

# Carpeta de trabajo
CARPETA = "docs/temp"

def main():
    # Pestañas principales
    tabs = st.tabs(["Carga de Información", "Filtrado", "Visualización"])

    # Pestaña: Carga de Información
    with tabs[0]:
        carga.cargar_informacion(CARPETA)

    # Pestaña: Filtrado
    with tabs[1]:
        filtrado.filtrado_informacion(CARPETA)

    # Pestaña: Visualización
    with tabs[2]:
        visualizacion.visualizacion_datos(CARPETA)

if __name__ == "__main__":
    main()
