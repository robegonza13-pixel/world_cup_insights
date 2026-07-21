# World Cup Insights
## Descripción

World Cup Insights es un sistema desarrollado en Python utilizando Programación Orientada a Objetos para analizar los partidos de la Copa Mundial de la FIFA.

El sistema descarga los datos desde un archivo CSV público, los procesa mediante Pandas, realiza análisis exploratorio de datos (EDA), genera estadísticas y crea visualizaciones para identificar tendencias e información relevante de los mundiales entre 1930 y 2022.

## Funcionalidades

- Descarga automática del dataset.
- Filtrado de partidos de la Copa Mundial.
- Limpieza y procesamiento de datos.
- Consultas por año, selección y país sede.
- Generación de estadísticas descriptivas.
- Exportación del dataset procesado.
- Visualización mediante histogramas, gráficos de barras, scatter plots y heatmaps.


## Tecnologías

- Python 3.14
- Pandas
- Matplotlib
- Seaborn
- NumPy
- Jupyter Notebook

## Estructura del proyecto

```text
world_cup_insights/
├── src/
│   ├── ingesta/
│   ├── gestor/
│   ├── eda/
│   ├── visualizacion/
│   ├── helpers/
│   └── main.py
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Visualizacion.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── app.py
│
└── README.md
```
## Instalación

1. Clonar el repositorio.
2. Instalar las dependencias:

```bash
pip install pandas matplotlib seaborn numpy jupyter
```

## Ejecución

El análisis del proyecto se encuentra en los siguientes notebooks:

- `notebooks/01_EDA.ipynb`
- `notebooks/02_Visualizacion.ipynb`

Opcionalmente, el proyecto puede ejecutarse desde:

```bash
python src/main.py
```

## Clases principales

### `CargadorDatos`

Responsable de la descarga, carga y persistencia de los datos.

**Funciones principales:**
- Descargar el dataset desde la URL pública.
- Filtrar únicamente los partidos de la Copa Mundial de la FIFA.
- Cargar el archivo CSV en un DataFrame de Pandas.
- Guardar los datos en `data/raw/` y `data/processed/`.

---

### `GestorPartidos`

Proporciona métodos de consulta sobre el conjunto de datos sin modificar la información.

**Funciones principales:**
- Buscar partidos por equipo.
- Consultar partidos por año.
- Consultar partidos por país sede.
- Obtener información de un partido específico.
- Realizar consultas estadísticas sobre los encuentros.

---

### `ProcesadorEDA`

Realiza el análisis exploratorio y el procesamiento de los datos.

**Funciones principales:**
- Limpieza de datos.
- Creación de columnas derivadas (año, total de goles, diferencia de goles y ganador).
- Generación de estadísticas descriptivas.
- Cálculo de la matriz de correlación.
- Agrupaciones y análisis por edición del Mundial.
- Detección de valores atípicos.

---

### `Visualizador`

Genera las visualizaciones utilizadas para el análisis de los datos.

**Funciones principales:**
- Histogramas.
- Gráficos de barras.
- Scatter plots.
- Heatmaps.
- Otras visualizaciones para mostrar tendencias y comparaciones.

---



## Autores
- Roberto Gonzalez gomez

Curso: Programación II
Colegio Universitario de Cartago