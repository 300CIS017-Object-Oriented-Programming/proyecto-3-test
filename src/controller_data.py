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
        self.__consolidado = pd.DataFrame()
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

    def filtrar_datos(self, anios, keyword):
        programas_agregados = set()
        for tipo in self.__data_sets:
            for anio in anios:
                data_frame = self.__data_sets[tipo][anio]
                if 'PROGRAMA_ACADEMICO' in data_frame.columns:
                    filas_filtradas = data_frame[
                        data_frame['PROGRAMA_ACADEMICO'].str.contains(keyword, case=False, na=False)]
                    for _, fila in filas_filtradas.iterrows():
                        programa = fila['PROGRAMA_ACADEMICO']
                        if programa not in programas_agregados:
                            programas_agregados.add(programa)
                            fila['AÑO'] = anio
                            self.__data_frame_filtrado = pd.concat([self.__data_frame_filtrado, fila.to_frame().T])

    def _obtener_primer_valor(self, columna, programa):
        df_programa_filtrado = self.__data_frame_filtrado[
            self.__data_frame_filtrado['PROGRAMA_ACADEMICO'] == programa]

        if not df_programa_filtrado.empty and columna in df_programa_filtrado.columns:
            return df_programa_filtrado[columna].iloc[0]
        return None

    def generar_consolidado(self, anios):
        consolidado = pd.DataFrame()

        for programa in self.__data_frame_filtrado['PROGRAMA_ACADEMICO'].unique():
            fila = {
                'PROGRAMA_ACADEMICO': programa,
                'MODALIDAD': self._obtener_primer_valor('MODALIDAD', programa),
                'ID_SEXO': self._obtener_primer_valor('ID_SEXO', programa),
                'SEXO': self._obtener_primer_valor('SEXO', programa),
                'NIVEL_FORMACION': self._obtener_primer_valor('NIVEL_FORMACION', programa),
            }

            for tipo in self.__data_sets.keys():
                for anio in anios:
                    if anio in self.__data_sets[tipo]:
                        df_tipo_anio = self.__data_sets[tipo][anio]
                        df_tipo_anio_programa = df_tipo_anio[df_tipo_anio['PROGRAMA_ACADEMICO'] == programa]
                        fila[f'{tipo.upper()}_{anio}'] = df_tipo_anio_programa[tipo.upper()]
                    else:
                        fila[f'{tipo.upper()}_{anio}'] = 0

            consolidado = pd.concat([consolidado, pd.DataFrame([fila])], ignore_index=True)

        self.__consolidado = consolidado









