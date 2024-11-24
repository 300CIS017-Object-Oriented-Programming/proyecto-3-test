[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3

## Documentación del Diagrama de Clases

### web_app
- **Métodos:**
  - `render_web()`: Este método se encarga de renderizar la interfaz web de la aplicación.

### data_controller
- **Atributos:**
  - `data_frame_programas`: Un DataFrame que contiene los datos de los programas académicos.
  - `datasets`: Un diccionario donde la clave es el tipo de dato ("admitidos", "matriculados", "neos", "graduados", "inscritos") y el valor es otro diccionario cuyas claves son el año de análisis ("2022") y el valor es el DataFrame asociado a dicho tipo de dato y año.
  - `data_frame_general`: Un DataFrame que contiene todos los datos consolidados.
- **Métodos:**
  - `filter_data(keyword: str)`: Filtra los programas académicos por nombre utilizando una palabra clave y retorna un DataFrame con los resultados.
  - `import_data(gestor: gestor_datos, folder: str, filename: str)`: Importa datos utilizando un gestor de datos específico desde una carpeta y archivo dados.
  - `export_data(gestor: gestor_datos, folder: str, filename: str)`: Exporta datos utilizando un gestor de datos específico a una carpeta y archivo dados.
  - `add_to_dataset(key: str, dataframe: DataFrame)`: Añade un DataFrame a un conjunto de datos identificado por una clave.
  - `get_dataset(key: str)`: Retorna una lista de DataFrames asociados a una clave específica.

### file_manager
- **Métodos:**
  - `list_files(folder: str)`: Lista los archivos en una carpeta dada y retorna una lista de nombres de archivos.
  - `create_folder(folder: str)`: Crea una carpeta con el nombre especificado.
  - `get_file_path(folder: str, filename: str)`: Retorna la ruta completa de un archivo dado su carpeta y nombre.
  - `get_all_file_paths(folder: str)`: Retorna una lista de todas las rutas de archivos en una carpeta dada.
  - `is_valid_file_name(filename: str)`: Verifica si un nombre de archivo es válido.

### gestor_datos
- **Métodos:**
  - `importar_datos(filepath: str)`: Importa datos desde una ruta de archivo y retorna un DataFrame.
  - `exportar_datos(data: DataFrame, filepath: str)`: Exporta un DataFrame a una ruta de archivo.

### gestor_csv (Hereda de gestor_datos)
- **Métodos:**
  - `importar_datos(filepath: str)`: Importa datos desde un archivo CSV y retorna un DataFrame.
  - `exportar_datos(data: DataFrame, filepath: str)`: Exporta un DataFrame a un archivo CSV.

### gestor_xlsx (Hereda de gestor_datos)
- **Métodos:**
  - `importar_datos(filepath: str)`: Importa datos desde un archivo XLSX y retorna un DataFrame.
  - `exportar_datos(data: DataFrame, filepath: str)`: Exporta un DataFrame a un archivo XLSX.

### gestor_json (Hereda de gestor_datos)
- **Métodos:**
  - `importar_datos(filepath: str)`: Importa datos desde un archivo JSON y retorna un DataFrame.
  - `exportar_datos(data: DataFrame, filepath: str)`: Exporta un DataFrame a un archivo JSON.

### Relaciones
- `web_app` administra `data_controller`.
- `data_controller` usa `file_manager` para gestionar archivos.
- `data_controller` usa `gestor_datos` para gestionar datos.
- `gestor_datos` es heredado por `gestor_csv`, `gestor_xlsx` y `gestor_json` para manejar diferentes formatos de archivo.


```mermaid
classDiagram
    class web_app {
        +render_web() void
    }
    
    class data_controller {
        -data_programas: DataFrame
        -datasets: dict<str, dict<str, DataFrame>>  
        -data_frame_general: DataFrame 
        +filter_data_keyword(keyword: str) DataFrame  
        +import_data(gestor: gestor_datos, folder: str, filename: str) void
        +export_data(gestor: gestor_datos, folder: str, filename: str) void
        +add_to_dataset(key: str, dataframe: DataFrame) void
        +get_dataset(key: str) list<DataFrame>
    }
    
    class file_manager {
        +list_files(folder: str) list<str>
        +create_folder(folder: str) void
        -get_file_path(folder: str, filename: str) str
        +get_all_file_paths(folder: str) list<str>
        -is_valid_file_name(filename: str) bool
    }
    
    class gestor_datos {
        +importar_datos(filepath: str) DataFrame
        +exportar_datos(data: DataFrame, filepath: str) void
    }
    
    class gestor_csv {
        +importar_datos(filepath: str) DataFrame
        +exportar_datos(data: DataFrame, filepath: str) void
    }
    
    class gestor_xlsx {
        +importar_datos(filepath: str) DataFrame
        +exportar_datos(data: DataFrame, filepath: str) void
    }
    
    class gestor_json {
        +importar_datos(filepath: str) DataFrame
        +exportar_datos(data: DataFrame, filepath: str) void
    }
    
    web_app --> data_controller : "Administra"
    data_controller --> file_manager : "Usa para gestionar archivos"
    data_controller --> gestor_datos : "Usa para gestionar datos"
    gestor_datos <|-- gestor_csv : "Hereda"
    gestor_datos <|-- gestor_xlsx : "Hereda"
    gestor_datos <|-- gestor_json : "Hereda"

