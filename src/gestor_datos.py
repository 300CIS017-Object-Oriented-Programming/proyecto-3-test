from abc import ABC, abstractmethod
import pandas as pd

#Clase abstracta para gestionar la importación y exportación de datos en diferentes formatos.
class gestor_datos(ABC):

    @abstractmethod
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        """
        Importa datos desde un archivo y los retorna como un DataFrame.

        :param ruta: La ruta del archivo a importar.
        :return: Un DataFrame con los datos importados.
        """
        pass

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
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        try:
            return pd.read_csv(ruta)
        except Exception as e:
            raise ValueError(f"Error al importar el archivo CSV: {e}")

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        try:
            datos.to_csv(ruta, index=False)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo CSV: {e}")



# Clase para gestionar archivos JSON
class gestor_json(gestor_datos):
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        try:
            return pd.read_json(ruta)
        except Exception as e:
            raise ValueError(f"Error al importar el archivo JSON: {e}")

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        try:
            datos.to_json(ruta, orient='records', lines=True)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo JSON: {e}")



# Clase para gestionar archivos XLSX
class gestor_xlsx(gestor_datos):
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        """
        Importa datos desde un archivo XLSX.
        """
        try:
            return pd.read_excel(ruta)
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