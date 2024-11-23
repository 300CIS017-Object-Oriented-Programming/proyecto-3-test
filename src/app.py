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

# Función para cargar y combinar datos de los archivos disponibles
def cargar_datos(carpeta):
    archivos = listar_archivos(carpeta)
    dataframes = []
    for archivo in archivos:
        file_path = os.path.join(carpeta, archivo)
        try:
            df = pd.read_excel(file_path)
            dataframes.append(df)
        except Exception as e:
            st.warning(f"Error al leer el archivo {archivo}: {e}")
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    return pd.DataFrame()  # Retorna un DataFrame vacío si no hay datos

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

    # Cargar y combinar datos
    datos = cargar_datos(carpeta)

    # Barra de búsqueda
    st.header("Búsqueda de Programas Académicos")
    palabra_clave = st.text_input("Ingresa palabras clave para buscar programas académicos:")

    if not datos.empty:
        if palabra_clave:
            # Filtrar datos que contengan las palabras clave en cualquier columna
            resultados = datos[
                datos.apply(lambda row: row.astype(str).str.contains(palabra_clave, case=False).any(), axis=1)
            ]
            if not resultados.empty:
                st.write("Resultados encontrados:")
                st.dataframe(resultados)
            else:
                st.write("No se encontraron resultados para la búsqueda.")
        else:
            st.write("Ingresa una palabra clave para comenzar la búsqueda.")
    else:
        st.write("No hay datos disponibles para buscar.")

if __name__ == "__main__":
    main()
