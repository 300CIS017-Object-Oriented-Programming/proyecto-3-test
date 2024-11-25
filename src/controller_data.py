from gestor_datos import gestor_datos, gestor_csv, gestor_json, gestor_xlsx
from gestor_archivos import gestor_archivos, obtener_type_year
from collections import defaultdict
import pandas as pd
import plotly.express as px


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

    def exportar_consolidado(self):
        gestor = self.__gestores_datos[0]
        gestor.exportar_datos(self.__consolidado, "../docs/outputs/consolidado.xlsx")

    def exportar_filtrado(self):
        gestor = self.__gestores_datos[0]
        gestor.exportar_datos(self.__data_frame_filtrado, "../docs/outputs/filtrado.xlsx")

    def grafica_linea_consolidado(self, tipo):
        columnas_tipo = [col for col in self.__consolidado.columns if col.startswith(tipo.upper())]
        if not columnas_tipo:
            print(f"No se encontraron columnas para el tipo '{tipo}'.")
            return

        data = []
        for _, fila in self.__consolidado.iterrows():
            programa = fila['PROGRAMA_ACADEMICO']
            for columna in columnas_tipo:
                anio = int(columna.split('_')[-1])
                valor = fila[columna]
                data.append({'Programa Académico': programa, 'Año': anio, 'Cantidad': valor})

        df_grafico = pd.DataFrame(data)

        fig = px.line(
            df_grafico,
            x='Año',
            y='Cantidad',
            color='Programa Académico',
            title=f'Evolución de {tipo.capitalize()} por Programa Académico',
            labels={'Año': 'Año', 'Cantidad': f'{tipo.capitalize()}', 'Programa Académico': 'Programa Académico'}
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(template='plotly_white',
                          title_text=f'Evolución de {tipo.capitalize()} por Programa Académico')
        fig.show()

    def graficos_comparativos_modalidad(self, programas_academicos, tipo):
        tipo_upper = tipo.upper()

        # Validar si las columnas correspondientes al tipo están en el consolidado
        columnas_tipo = [col for col in self.__consolidado.columns if col.startswith(tipo_upper)]
        if not columnas_tipo:
            print(f"No se encontraron columnas para el tipo '{tipo}' en el consolidado.")
            return

        data = []
        for programa in programas_academicos:
            df_programa = self.__consolidado[self.__consolidado['PROGRAMA_ACADEMICO'] == programa]
            if df_programa.empty:
                print(f"No se encontró información para el programa académico: {programa}")
                continue

            modalidad = df_programa['MODALIDAD'].iloc[0] if 'MODALIDAD' in df_programa.columns else 'Desconocida'

            for columna in columnas_tipo:
                anio = int(columna.split('_')[-1])  # Extraer el año de la columna
                valor = df_programa[columna].iloc[0] if columna in df_programa.columns else 0
                data.append({
                    'Programa Académico': programa,
                    'Modalidad': modalidad,
                    'Año': anio,
                    'Cantidad': valor
                })

        df_grafico = pd.DataFrame(data)

        fig = px.bar(
            df_grafico,
            x='Año',
            y='Cantidad',
            color='Modalidad',
            facet_row='Programa Académico',
            title=f'Gráfico comparativo por modalidad: {tipo}',
            labels={'Año': 'Año', 'Cantidad': 'Cantidad', 'Modalidad': 'Modalidad'}
        )

        fig.update_layout(
            template='plotly_white',
            title_text=f'Gráfico comparativo por modalidad: {tipo}',
            title_x=0.5,
            height=600 + 200 * len(programas_academicos),
        )

        fig.show()











