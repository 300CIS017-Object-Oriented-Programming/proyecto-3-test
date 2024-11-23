import streamlit as st
import pandas as pd
import os

# Función para cargar el CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Función para listar archivos disponibles
def listar_archivos(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)  # Crear la carpeta si no existe
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".xlsx")]
    return archivos

def main():
    # Llamar la función para cargar el CSS
    load_css("estilos.css")

    # Contenedor principal para organizar el layout
    st.markdown(
        """
        <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
            <div>
                <h1>Data Manager</h1>
                <p>Bienvenido a Data Manager. 
                <p>Aquí puedes gestionar tus datos de manera rápida y sencilla</p>
            </div>
            <div style='margin-left: 20px;'>
                <img src='https://cdn-icons-png.flaticon.com/512/4675/4675644.png' width='180' height='180'>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Mostrar lista de archivos disponibles
    st.header("Archivos disponibles")
    carpeta = "temp"
    archivos_disponibles = listar_archivos(carpeta)
    if archivos_disponibles:
        for archivo in archivos_disponibles:
            st.write(f"- {archivo}")
    else:
        st.write("No hay archivos disponibles.")

    # Subir un nuevo archivo
    st.header("Carga de nuevos archivos")
    uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])

    if uploaded_file:
        # Guardar el archivo en la carpeta temporal
        with open(f"{carpeta}/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Archivo {uploaded_file.name} cargado correctamente.")

        # Vista previa del archivo
        data = pd.read_excel(uploaded_file)
        st.write("Vista previa de los datos:")
        st.dataframe(data)

if __name__ == "__main__":
    main()

