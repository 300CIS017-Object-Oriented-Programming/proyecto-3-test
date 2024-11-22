import streamlit as st
import pandas as pd



def main() :
   import streamlit as st

   # Función para cargar el CSS
   def load_css(file_name):
      with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

   # Cargar el CSS
   load_css("estilos.css")

   # Título de la aplicación
   st.markdown('<h1>Data Manager</h1>', unsafe_allow_html=True)

   st.write("Bienvenido a Data Manager. Aquí puedes gestionar tus datos de manera rapida y sencilla")

   uploaded_file = st.file_uploader("Sube tus archivos Excel aquí", type=["xlsx"])

   if uploaded_file:
      data = pd.read_excel(uploaded_file)
      st.write("Vista previa de los datos:")
      st.dataframe(data)
      # Guarda temporalmente
      with open(f"temp/{uploaded_file.name}", "wb") as f:
         f.write(uploaded_file.getbuffer())


# APARTADO PARA CARGAR LOS ARCHIVOS

   if st.button("Buscar Programas"):
      keyword = st.text_input("Ingresa palabras clave")
      if keyword:
         filtered_data = data[data["Programa"].str.contains(keyword, case=False, na=False)]
         st.write("Resultados de la búsqueda:")
         st.dataframe(filtered_data)

         selected_programs = st.multiselect(
            "Selecciona programas para análisis",
            options=filtered_data["Programa"].unique(),
         )
         st.write("Programas seleccionados:", selected_programs)


#APARTADO PARA FILTRAR LA INFORMACION



#APARTADO PARA PROCESAMIENTO DE DATOS
   years = st.slider("Selecciona el rango de años", min_value=2018, max_value=2023, value=(2020, 2023))



main()

