import streamlit as st
from gestor_archivos import gestor_archivos


def cargar_informacion(controller):
    """Página para cargar archivos."""
    st.header("Carga de Información")

    # Listar archivos disponibles
    st.subheader("Archivos disponibles:")
    gestor_archivos_init = gestor_archivos()
    archivos_disponibles = gestor_archivos_init.obtener_todas_las_rutas_archivos()
    if archivos_disponibles:
        st.write(archivos_disponibles)
    else:
        st.write("No hay archivos disponibles.")

    # Subir un nuevo archivo
    st.subheader("Carga de nuevos archivos:")
    uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])
    controller.importar_datos(uploaded_file)
    if uploaded_file:
        st.success(f"Archivo {uploaded_file.name} cargado correctamente.")

