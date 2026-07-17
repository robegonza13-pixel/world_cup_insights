from ingesta.carga import CargadorDatos
from gestor.gestion import GestorPartidos

url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
cargador = CargadorDatos(url, r"C:\world_cup_insights\data\raw", r"C:\world_cup_insights\data\processed")

df = cargador.descarga()
print("Descargado:", df.shape)

df_mundial = cargador.filtro()
print("Filtrado mundial:", df_mundial.shape)

ruta = cargador.guardar_raw()
print("Guardado en:", ruta)

ejemplo = GestorPartidos(df_mundial)
print(ejemplo.get_partido(40))
print(ejemplo.get_por_equipo('Argentina'))
print(ejemplo.get_por_anio(2014))
print(ejemplo.get_por_sede('Germany'))
print(ejemplo.ventaja_local())
print(ejemplo.get_campeones())
print(ejemplo.get_enfrentamientos_directos('Argentina', 'France'))