import pandas as pd
import numpy as np
class GestorPartidos:
    def __init__(self, df):
        self.__df = df

    def get_partido(self, id_partido):
        partido = self.__df[self.__df['id_partido'] == id_partido]
        return partido

    def get_por_equipo(self, nombre_equipo):
        df_equipo = self.__df[(self.__df['home_team'] == nombre_equipo) | (self.__df['away_team'] == nombre_equipo)]
        return df_equipo

    def get_por_anio(self, anio):
        fechas = pd.to_datetime(self.__df['date'])
        df_anio = self.__df[fechas.dt.year == anio]
        return df_anio

    def get_por_sede(self, sede):
        df_sede = self.__df[self.__df['country'] == sede]
        return df_sede

    def ventaja_local(self):
        df_no_neutral = self.__df[self.__df['neutral'] == False]
        resultado = np.where(
            df_no_neutral['home_score'] > df_no_neutral['away_score'], 'local',
            np.where(df_no_neutral['home_score'] < df_no_neutral['away_score'], 'visitante', 'empate')
        )
        porcentajes = pd.Series(resultado).value_counts(normalize=True) * 100
        return porcentajes