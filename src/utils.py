import os
import pandas as pd

# Rango de años permitido
YEAR_MIN = 1990
YEAR_MAX = 2024

def listar_archivos(carpeta):
    """Lista los archivos disponibles en la carpeta."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)  # Crear la carpeta si no existe
    return [f for f in os.listdir(carpeta) if f.endswith(".xlsx")]

def cargar_datos(carpeta):
    """Carga y combina datos de los archivos disponibles en la carpeta."""
    archivos = listar_archivos(carpeta)
    dataframes = []
    for archivo in archivos:
        file_path = os.path.join(carpeta, archivo)
        try:
            df = pd.read_excel(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f"Error al leer el archivo {archivo}: {e}")
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    return pd.DataFrame()
