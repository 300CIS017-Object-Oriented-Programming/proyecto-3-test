import streamlit as st
from utils import cargar_datos, YEAR_MIN, YEAR_MAX

def filtrado_informacion(carpeta):
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

    # Cargar datos y filtrar por años
    datos = cargar_datos(carpeta)
    if not datos.empty:
        st.write("Datos cargados:")
        st.dataframe(datos)

        # Filtrar según el rango de años seleccionado
        if "Año" in datos.columns:
            filtrados = datos[
                (datos["Año"] >= selected_years[0]) & (datos["Año"] <= selected_years[1])
            ]
            st.write("Datos filtrados:")
            st.dataframe(filtrados)
        else:
            st.warning("Los datos no contienen una columna llamada 'Año'.")
    else:
        st.warning("No hay datos disponibles. Regresa a la pestaña de carga para cargar datos.")

