from gestor_datos import gestor_datos, gestor_csv, gestor_json, gestor_xlsx
from gestor_archivos import gestor_archivos, obtener_type_year
from collections import defaultdict
import pandas as pd

class controller_data:
    def __init__(self):
        self.__gestores_datos = [gestor_xlsx(), gestor_csv(), gestor_json()]
        self.__programas_data = pd.DataFrame()
        self.__gestor_archivos = gestor_archivos()
        self.__data_sets = defaultdict(dict)
        self.__data_frame_filtrado = pd.DataFrame()

    def importar_datos(self, archivo):
        ruta = f"{self.__gestor_archivos.carpeta_temp}/{archivo.name}"
        tipo, anio = obtener_type_year(archivo)
        self.__gestor_archivos.agregar_archivo(archivo)
        gestor = self.__gestores_datos[0]
        data_frame = gestor.importar_datos(ruta)
        self.__data_sets[tipo][anio] = data_frame
        columna_id_sexo_index = data_frame.columns.get_loc('ID_SEXO')
        df_copy = data_frame.iloc[:, :columna_id_sexo_index].copy()
        self.__programas_data = pd.concat([self.__programas_data, df_copy])

    def exportar_datos(self, tipo):
        gestor = self.__gestores_datos[tipo]
        extension = ""
        if tipo == 0:
            extension = "xlsx"
        if tipo == 1:
            extension = "json"
        if tipo == 2:
            extension = "csv"
        gestor.exportar_datos(self.__data_frame_filtrado, f"../docs/outputs/data_filtrado." + extension)

    def




