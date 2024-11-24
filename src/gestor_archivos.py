import os

def _es_nombre_valido(nombre_archivo):
    prefijos_validos = ["admitidos", "matriculados", "inscritos", "neos", "graduados"]
    years_validos = [str(year) for year in range(1990, 2025)]

    if not nombre_archivo.endswith(".xlsx"):
        return False

    base_name = nombre_archivo.rsplit(".", 1)[0]

    for prefijo in prefijos_validos:
        if base_name.startswith(prefijo):
            for year in years_validos:
                if base_name.endswith(year):
                    return True

    return False

class gestor_archivos:
    def __init__(self, carpeta_default = "docs/default", carpeta_temp = "docs/temp"):
        self.carpeta_default = carpeta_default
        self.carpeta_temp = carpeta_temp

    def obtener_rutas_default(self):
        return [f for f in os.listdir(self.carpeta_default) if _es_nombre_valido(f)]

    def obtener_rutas_temp(self):
        return [f for f in os.listdir(self.carpeta_temp) if _es_nombre_valido(f)]

    def obtener_todas_las_rutas_archivos(self):
        return self.obtener_rutas_default().extend(self.obtener_rutas_temp())

    def agregar_archivo(self, archivo, temporal=True):
        carpeta = self.carpeta_temp if temporal else self.carpeta_default
        with open(f"{carpeta}/{archivo.name}", "wb") as f:
            f.write(archivo.getbuffer())

    def eliminar_archivo(self, archivo, temporal=True):
        carpeta = self.carpeta_temp if temporal else self.carpeta_default
        os.remove(f"{carpeta}/{archivo}")
