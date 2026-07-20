import pandas as pd
import os

class CargadorDatos:
    def __init__(self, url, carpeta_raw, carpeta_processed):
        self.__url = url
        self.__carpeta_raw = carpeta_raw
        self.__carpeta_processed = carpeta_processed
        self.__df = None
        self.__df_mundial = None

    def descarga(self):
        self.__df = pd.read_csv(self.__url, header=0, sep=',', encoding='UTF-8')
        return self.__df

    def filtro(self):
        self.__df_mundial = self.__df[self.__df['tournament'] == 'FIFA World Cup'].copy()
        self.__df_mundial = self.__df_mundial.reset_index(drop=True)
        self.__df_mundial['id_partido'] = range(1, len(self.__df_mundial) + 1)
        columnas = self.__df_mundial.columns.tolist()
        columnas.remove('id_partido')
        nuevo_orden = ['id_partido'] + columnas
        self.__df_mundial = self.__df_mundial[nuevo_orden]
        return self.__df_mundial

    def guardar_raw(self):
        ruta_completa = os.path.join(self.__carpeta_raw, "partidos-mundial.csv")
        self.__df_mundial.to_csv(ruta_completa, index=False)
        return ruta_completa

    def guardar_processed(self, df_procesado):
        ruta_completa = os.path.join(self.__carpeta_processed, "partidos-mundial-procesado.csv")
        df_procesado.to_csv(ruta_completa, index=False)
        return ruta_completa