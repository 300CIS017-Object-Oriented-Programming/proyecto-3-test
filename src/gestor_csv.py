from gestor_datos import gestor_datos
import pandas as pd

# Clase para gestionar archivos CSV
class gestor_csv(gestor_datos):
    def importar_datos(self, ruta: str) -> pd.DataFrame:
        """
        Importa datos desde un archivo CSV.
        """
        try:
            return pd.read_csv(ruta)
        except Exception as e:
            raise ValueError(f"Error al importar el archivo CSV: {e}")

    def exportar_datos(self, datos: pd.DataFrame, ruta: str) -> None:
        """
        Exporta un DataFrame a un archivo CSV.
        """
        try:
            datos.to_csv(ruta, index=False)
        except Exception as e:
            raise ValueError(f"Error al exportar el archivo CSV: {e}")