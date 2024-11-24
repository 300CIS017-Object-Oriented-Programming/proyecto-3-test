from gestor_datos import gestor_datos
import pandas as pd

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