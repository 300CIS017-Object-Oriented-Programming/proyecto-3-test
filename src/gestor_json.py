from gestor_datos import gestor_datos
import pandas as pd

# Clase para gestionar archivos JSON
class gestor_json(gestor_datos):
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        """
        Importa datos desde un archivo JSON.
        """
        try:
            return pd.read_json(ruta)
        except Exception as e:
            raise ValueError(f"Error al importar el archivo JSON: {e}")

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        """
        Exporta un DataFrame a un archivo JSON.
        """
        try:
            datos.to_json(ruta, orient='records', lines=True)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo JSON: {e}")