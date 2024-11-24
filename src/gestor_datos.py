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
