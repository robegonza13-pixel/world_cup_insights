from ingesta.carga import CargadorDatos

url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
cargador = CargadorDatos(url, r"C:\world_cup_insights\data\raw", r"C:\world_cup_insights\data\processed")

df = cargador.descarga()
print("Descargado:", df.shape)

df_mundial = cargador.filtro()
print("Filtrado mundial:", df_mundial.shape)
print(df_mundial['tournament'].unique())

ruta = cargador.guardar_raw()
print("Guardado en:", ruta)