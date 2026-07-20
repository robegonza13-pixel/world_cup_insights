from ingesta.carga import CargadorDatos
from gestor.gestion import GestorPartidos
from eda.analisis_eda import ProcesadorEDA
from visualizacion.visualizaciones import Visualizador


url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
cargador = CargadorDatos(url, r"C:\world_cup_insights\data\raw", r"C:\world_cup_insights\data\processed")
print('Prueba CargadorDatos\n')

cargador.descarga()
print('Descarga exitosa\n')

df_mundial = cargador.filtro()
print('Filtro aplicado al dataframe\n')

cargador.guardar_raw()
print('Archivo guardado en carpeta /raw\n')

print('Prueba GestorPartido\n')

gestor = GestorPartidos(df_mundial)

print(gestor.get_partido(1030))
print(gestor.get_por_equipo('Brazil'))
print(gestor.get_por_anio(2022))
print(gestor.get_por_sede('Mexico'))
print(gestor.ventaja_local())
print(gestor.get_enfrentamientos_directos('Costa Rica', 'Brazil'))
print(gestor.get_campeones())

print('\nPrueba ProcesadorEDA \n')

procesador = ProcesadorEDA(df_mundial)

procesador.limpieza_datos()
print('Limpieza de datos aplicada\n')

df_final = procesador.agregar_columnas_derivadas()
print('Columnas derivadas agregadas')

cargador.guardar_processed(df_final)
print('Datos procesados almacenados en carpeta /processed\n')

print(procesador.resumen_descriptivo())

print(procesador.matriz_correlacion())

outliers = procesador.deteccion_outliers('total_goles')
print(outliers)

print(procesador.agrupacion_por_edicion())

print('\nPrueba Visualizador \n')
graficos = Visualizador()
graficos.histograma(df_final, 'total_goles', titulo='Distribución de goles totales por partido' )

df_ediciones = procesador.agrupacion_por_edicion()
graficos.grafico_barras(df_ediciones.reset_index(), 'anio', 'promedio_goles_partido', titulo='Goles promedio por Mundial')

matriz = procesador.matriz_correlacion()
graficos.heatmap(matriz, titulo='Correlación entre variables')

graficos.boxplot(df_final, 'total_goles', titulo='Outliers en goles totales')

graficos.scatter(df_final, 'anio', 'total_goles', titulo='Goles totales por partido a través de los años')

graficos.grafico_lineas(df_ediciones.reset_index(),'anio','total_goles_edicion',
titulo='Evolución del total de goles anotados por Mundial'
)