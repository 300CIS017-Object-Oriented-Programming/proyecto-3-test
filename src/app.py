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
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".xlsx")]  # Nombre-Area
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

# Función principal para cada pestaña
def cargar_informacion(carpeta, current_page):
    st.header("Carga de Información")
    st.write("Aquí puedes cargar y eliminar archivos Excel para gestionarlos.")

    # Listar archivos disponibles
    archivos_disponibles = listar_archivos(carpeta)
    st.subheader("Archivos disponibles:")
    if archivos_disponibles:
        for archivo in archivos_disponibles:
            st.write(f"- {archivo}")
    else:
        st.write("No hay archivos disponibles.")

    # Subir un nuevo archivo
    st.subheader("Carga de nuevos archivos:")
    uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])
    if uploaded_file:
        # Guardar el archivo en la carpeta temporal
        with open(f"{carpeta}/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Archivo {uploaded_file.name} cargado correctamente.")

    # Botón para avanzar a la siguiente pestaña
    if st.button("Ir al filtrado de información"):
        st.session_state["page"] = "Filtrado"

def filtrado_informacion(carpeta):
    st.header("Filtrado de Información")
    st.write("Busca programas académicos por palabras clave en los datos cargados.")

    # Cargar datos
    datos = cargar_datos(carpeta)
    if datos.empty:
        st.warning("No hay datos disponibles. Regresa a la pestaña anterior para cargar datos.")
        return

    # Barra de búsqueda
    palabra_clave = st.text_input("Ingresa palabras clave para buscar programas académicos:")
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

    # Botón para avanzar a la siguiente pestaña
    if st.button("Ir a la visualización de datos"):
        st.session_state["page"] = "Visualización"

def visualizacion_datos(carpeta):
    st.header("Visualización de Datos")
    st.write("Aquí puedes visualizar todos los datos cargados.")

    # Cargar datos
    datos = cargar_datos(carpeta)
    if datos.empty:
        st.warning("No hay datos disponibles. Regresa a la pestaña anterior para cargar datos.")
        return

    # Mostrar los datos
    st.dataframe(datos)

    # Botón para regresar a la carga de información
    if st.button("Regresar a la carga de información"):
        st.session_state["page"] = "Carga"

# Lógica principal de la aplicación
def main():
    # Llamar la función para cargar el CSS
    load_css("estilos.css")

    # Crear un estado persistente para la navegación entre pestañas
    if "page" not in st.session_state:
        st.session_state["page"] = "Carga"

    # Carpeta de trabajo
    carpeta = "temp"

    # Navegación entre pestañas
    if st.session_state["page"] == "Carga":
        cargar_informacion(carpeta, st.session_state["page"])
    elif st.session_state["page"] == "Filtrado":
        filtrado_informacion(carpeta)
    elif st.session_state["page"] == "Visualización":
        visualizacion_datos(carpeta)

if __name__ == "__main__":
    main()
