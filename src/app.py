import streamlit as st
import pandas as pd

# Función para cargar el CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
                <p> Aquí puedes gestionar tus datos de manera rapida y sencilla </p>
            </div>
            <div style='margin-left: 20px;'>
                <img src='https://cdn-icons-png.flaticon.com/512/4675/4675644.png' width='180' height='180'>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])

    if uploaded_file:
        data = pd.read_excel(uploaded_file)
        st.write("Vista previa de los datos:")
        st.dataframe(data)
        # Guarda temporalmente
        with open(f"temp/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())

if __name__ == "__main__":
    main()
