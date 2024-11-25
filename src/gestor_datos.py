from abc import ABC, abstractmethod
import pandas as pd
import streamlit as st

#Clase abstracta para gestionar la importación y exportación de datos en diferentes formatos.
class gestor_datos(ABC):

    @abstractmethod
    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        """
        Exporta un DataFrame a un archivo en el formato correspondiente.

        :param datos: El DataFrame que se va a exportar.
        :param ruta: La ruta donde se almacenará el archivo exportado.
        """
        pass


# Clase para gestionar archivos CSV
class gestor_csv(gestor_datos):

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        try:
            datos.to_csv(ruta, index=False)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo CSV: {e}")



# Clase para gestionar archivos JSON
class gestor_json(gestor_datos):

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        try:
            datos.to_json(ruta, orient='records', lines=True)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo JSON: {e}")



# Clase para gestionar archivos XLSX
class gestor_xlsx(gestor_datos):
    @st.cache_data
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        """
        Importa datos desde un archivo XLSX.
        """
        try:
            pd_completo = pd.read_excel(ruta, sheet_name=None)

            # Determina la hoja a leer
            sheet_to_read = list(pd_completo.keys())[1] if len(pd_completo) > 1 else list(pd_completo.keys())[0]
            pd_completo = pd.read_excel(ruta, sheet_name=sheet_to_read)

            # Encuentra la fila que contiene "CÓDIGO DE LA INSTITUCIÓN" en la primera columna
            start_row = pd_completo[pd_completo.iloc[:, 0] == "CÓDIGO DE LA INSTITUCIÓN"].index[0]

            # Lee el archivo a partir de la fila encontrada
            return pd.read_excel(ruta, sheet_name=sheet_to_read, skiprows=start_row)
        except Exception as e:
            raise ValueError(f"Error al importar el archivo XLSX: {e}")

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        """
        Exporta un DataFrame a un archivo XLSX.
        """
        try:
            datos.to_excel(ruta, index=False)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo XLSX: {e}")