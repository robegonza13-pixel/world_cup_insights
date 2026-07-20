import pandas as pd
import numpy as np

class ProcesadorEDA:
    def __init__(self, df):
        self.__df = df

    def limpieza_datos(self):
        if self.__df.duplicated().sum() > 0:
            self.__df = self.__df.drop_duplicates()

        if self.__df.isna().sum().sum() > 0:
            self.__df = self.__df.dropna()

        self.__df['date'] = pd.to_datetime(self.__df['date'])
        self.__df['home_score'] = self.__df['home_score'].astype(int)
        self.__df['away_score'] = self.__df['away_score'].astype(int)

        return self.__df

    def agregar_columnas_derivadas(self):
        self.__df['anio'] = self.__df['date'].dt.year

        self.__df['total_goles'] = self.__df['home_score'] + self.__df['away_score']

        self.__df['diferencia_goles'] = abs(self.__df['home_score'] - self.__df['away_score'])

        self.__df['ganador'] = np.where(
            self.__df['home_score'] > self.__df['away_score'], 'Local',
            np.where(self.__df['away_score'] > self.__df['home_score'], 'Visitante', 'Empate')
        )

        return  self.__df

    def resumen_descriptivo(self):
        print(self.__df.info())
        describe_numerico = self.__df.iloc[:,1:].describe()
        describe_categorico=  self.__df.describe(include='object')

        total_partidos = len(self.__df)
        rango_anios = (self.__df['anio'].min(), self.__df['anio'].max())

        moda = self.__df.iloc[:, 1:].mode()

        return describe_numerico, describe_categorico, total_partidos, rango_anios, moda

    def matriz_correlacion(self):
        variables_numericas = self.__df.iloc[:,1:].select_dtypes(include='number')
        matriz_corr = variables_numericas.corr()
        return matriz_corr

    def deteccion_outliers(self, columna_numerica):
        q1 = self.__df[columna_numerica].quantile(0.25)
        q3 = self.__df[columna_numerica].quantile(0.75)

        ric = q3 - q1

        lim_inf = q1 - 1.5*ric
        lim_sup = q3 + 1.5*ric

        return self.__df[columna_numerica][(self.__df[columna_numerica] < lim_inf) | (self.__df[columna_numerica] > lim_sup)]

    def agrupacion_por_edicion(self):
        resultado = self.__df.groupby('anio').agg(
            total_goles_edicion=('total_goles', 'sum'),
            promedio_goles_partido=('total_goles', 'mean'),
            partidos_jugados=('id_partido', 'count')
        )
        return resultado