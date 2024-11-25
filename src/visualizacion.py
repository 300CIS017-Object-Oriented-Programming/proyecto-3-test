import streamlit as st
import matplotlib.pyplot as plt
from utils import cargar_datos

def visualizacion_datos(carpeta):
    """Página para visualizar datos cargados."""
    st.header("Visualización de Datos")

    # Mostrar todos los datos cargados
    datos = cargar_datos(carpeta)
    if not datos.empty:
        st.write("Datos cargados:")
        st.dataframe(datos)

        # Seleccionar columna para graficar
        columnas = datos.columns.tolist()
        columna_seleccionada = st.selectbox("Selecciona la columna para graficar", columnas)

        # Crear gráfico
        fig, ax = plt.subplots()
        datos[columna_seleccionada].value_counts().plot(kind='bar', ax=ax, color='skyblue')

        # Personalizar el gráfico
        ax.set_title(f"Distribución de {columna_seleccionada}", fontsize=16, fontweight='bold')
        ax.set_xlabel(columna_seleccionada, fontsize=14)
        ax.set_ylabel("Frecuencia", fontsize=14)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, linestyle='--', alpha=0.7)

        # Mostrar gráfico en Streamlit
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles. Regresa a la pestaña de carga para cargar datos.")