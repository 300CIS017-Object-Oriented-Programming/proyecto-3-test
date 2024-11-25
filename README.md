[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3

# Documentación del Diagrama de Clases

## **web_app**
- **Métodos:**
  - `renderizar_web()`: Renderiza la interfaz web de la aplicación.

---

## **controller_data**
- **Atributos:**
  - `programas_data`: Un DataFrame que contiene los datos principales de los programas académicos.
  - `datasets`: Un diccionario donde:
    - La clave es una cadena (`str`) que representa una categoría de datos (por ejemplo, `"admitidos"`, `"graduados"`, etc.).
    - El valor es otro diccionario que asocia cadenas (`str`) (como el año: `"2022"`) a DataFrames.
  - `data_frame_general`: Un DataFrame que consolida todos los datos de los diferentes conjuntos.
- **Métodos:**
  - `filtrar_datos_palabra_clave(palabra_clave: str) -> DataFrame`: Filtra los datos en base a una palabra clave y retorna un DataFrame con los resultados.
  - `importar_datos(gestor: gestor_datos, carpeta: str, archivo: str) -> None`: Importa datos desde un archivo específico utilizando un gestor de datos.
  - `exportar_datos(gestor: gestor_datos, carpeta: str, archivo: str) -> None`: Exporta datos a un archivo específico utilizando un gestor de datos.

---

## **gestor_archivos**
- **Métodos Públicos:**
  - `crear_carpeta(carpeta: str) -> None`: Crea una carpeta si no existe.
  - `obtener_rutas_default() -> list[str]`: Obtiene una lista de rutas de los archivos predeterminados.
  - `obtener_rutas_temporal() -> list[str]`: Obtiene una lista de rutas de los archivos temporales.
  - `obtener_todas_las_rutas_archivos() -> list[str]`: Obtiene una lista con todas las rutas de archivos, tanto predeterminados como temporales.
  - `agregar_archivo(archivo: str, temporal: bool) -> None`: Agrega un archivo a la carpeta 'temp' si la flag "temporal" es True, de lo contrario lo agrega a default.
  - `eliminar_archivo(archivo: str, temporal: bool) -> None`: Elimina un archivo de la carpeta 'temp' si la flag "temporal" es True, de lo contrario lo elimina de default.
- **Método Privado:**
  - `_es_nombre_valido(archivo: str) -> bool`: Verifica si un nombre de archivo cumple con las condiciones necesarias.

---

## **gestor_datos**
- **Métodos:**
  - `importar_datos(ruta: str) -> DataFrame`: Importa datos desde la ruta especificada y los retorna como un DataFrame.
  - `exportar_datos(datos: DataFrame, ruta: str) -> None`: Exporta un DataFrame a la ruta especificada.

---

## **gestor_csv** *(Hereda de gestor_datos)*
- **Métodos:**
  - `importar_datos(ruta: str) -> DataFrame`: Importa datos desde un archivo CSV.
  - `exportar_datos(datos: DataFrame, ruta: str) -> None`: Exporta un DataFrame a un archivo CSV.

---

## **gestor_xlsx** *(Hereda de gestor_datos)*
- **Métodos:**
  - `importar_datos(ruta: str) -> DataFrame`: Importa datos desde un archivo XLSX.
  - `exportar_datos(datos: DataFrame, ruta: str) -> None`: Exporta un DataFrame a un archivo XLSX.

---

## **gestor_json** *(Hereda de gestor_datos)*
- **Métodos:**
  - `importar_datos(ruta: str) -> DataFrame`: Importa datos desde un archivo JSON.
  - `exportar_datos(datos: DataFrame, ruta: str) -> None`: Exporta un DataFrame a un archivo JSON.

---

## **Relaciones**
- **`web_app`** administra **`controlador_datos`**.
- **`controlador_datos`** usa **`gestor_archivos`** para la gestión de archivos.
- **`controlador_datos`** usa **`gestor_datos`** para la manipulación de datos.
- **`gestor_datos`** es la clase base para **`gestor_csv`**, **`gestor_xlsx`**, y **`gestor_json`**, que implementan funcionalidades específicas para manejar diferentes formatos de archivo.


```mermaid
classDiagram
    class web_app {
        +renderizar_web() void
    }
    
    class controller_data {
        -programas_data: DataFrame
        -datasets: dict<str, dict<str, DataFrame>>  
        -data_frame_general: DataFrame 
        +filtrar_datos_palabra_clave(palabra_clave: str) DataFrame  
        +importar_datos(gestor: gestor_datos, carpeta: str, archivo: str) void
        +exportar_datos(gestor: gestor_datos, carpeta: str, archivo: str) void
        +agregar_a_conjunto_datos(clave: str, dataframe: DataFrame) void
        +obtener_data(clave: str) list<DataFrame>
    }
    
    class gestor_archivos {
        +crear_carpeta(carpeta: str) void
        +obtener_rutas_default() list<str>
        +obtener_rutas_temporal() list<str>
        +obtener_todas_las_rutas_archivos() list<str>
        +agregar_archivo(archivo: str) void
        +eliminar_archivo(archivo: str) void
        -es_nombre_valido(archivo: str) bool
    }
    
    class gestor_datos {
        +importar_datos(ruta: str) DataFrame
        +exportar_datos(datos: DataFrame, ruta: str) void
    }
    
    class gestor_csv {
        +importar_datos(ruta: str) DataFrame
        +exportar_datos(datos: DataFrame, ruta: str) void
    }
    
    class gestor_xlsx {
        +importar_datos(ruta: str) DataFrame
        +exportar_datos(datos: DataFrame, ruta: str) void
    }
    
    class gestor_json {
        +importar_datos(ruta: str) DataFrame
        +exportar_datos(datos: DataFrame, ruta: str) void
    }
    
    web_app --> controlador_datos : "Administra"
    controller_data --> gestor_archivos : "Usa para gestionar archivos"
    controller_data --> gestor_datos : "Usa para gestionar datos"
    gestor_datos <|-- gestor_csv : "Hereda"
    gestor_datos <|-- gestor_xlsx : "Hereda"
    gestor_datos <|-- gestor_json : "Hereda"


