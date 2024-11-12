[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3

```mermaid
classDiagram
    class WebApp {
        +renderWeb() void
    }

    class Controller {
        -dataFrame: DataFrame
        +filterData(condition) DataFrame
        +importData(gestor: GestorDatos, filepath: str) void
    }

    class GestorDatos {
        +exportarDatos(data: DataFrame, filepath: str) void
    }

    class GestorCsv {
        +exportarDatos(data: DataFrame, filepath: str) void
    }

    class GestorXLSX {
        +exportarDatos(data: DataFrame, filepath: str) void
        +importarDatos(filepath: str) DataFrame
    }

    class GestorJson {
        +exportarDatos(data: DataFrame, filepath: str) void
    }

    WebApp --> Controller : "administra"
    Controller --> GestorDatos : "usa para gestionar datos"
    Controller o--> GestorXLSX : "usa para importar datos"
    GestorDatos <|-- GestorCsv : "hereda"
    GestorDatos <|-- GestorXLSX : "hereda"
    GestorDatos <|-- GestorJson : "hereda"