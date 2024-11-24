import streamlit as st
from utils import listar_archivos

def cargar_informacion(carpeta):
    """Página para cargar archivos."""
    st.header("Carga de Información")

    # Listar archivos disponibles
    st.subheader("Archivos disponibles:")
    archivos_disponibles = listar_archivos(carpeta)
    if archivos_disponibles:
        st.write(archivos_disponibles)
    else:
        st.write("No hay archivos disponibles.")

    # Subir un nuevo archivo
    st.subheader("Carga de nuevos archivos:")
    uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])
    if uploaded_file:
        with open(f"{carpeta}/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Archivo {uploaded_file.name} cargado correctamente.")

