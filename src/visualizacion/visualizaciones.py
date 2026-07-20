import seaborn as sns
import matplotlib.pyplot as plt


class Visualizador:

    def histograma(self, datos, columna, titulo=None, barras='auto'):
        plt.figure(figsize=(8, 5))
        sns.histplot(data=datos, x=columna, bins=barras, kde=True, discrete=True)
        plt.title(titulo if titulo else f'Distribución de {columna}')
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        plt.show()

    def grafico_barras(self, datos, x, y, titulo=None):
        plt.figure(figsize=(8, 5))
        sns.barplot(data=datos, x=x, y=y)
        plt.title(titulo if titulo else f'{y} por {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xticks(rotation=45)
        plt.show()

    def grafico_lineas(self, datos, x, y, titulo=None):
        plt.figure(figsize=(8, 5))
        sns.lineplot(data=datos, x=x, y=y, marker='o')
        plt.title(titulo if titulo else f'{y} a través de {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def heatmap(self, matriz, titulo=None):
        plt.figure(figsize=(8, 6))
        sns.heatmap(matriz, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(titulo if titulo else 'Mapa de calor')
        plt.show()

    def scatter(self, datos, x, y, titulo=None, hue=None):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=datos, x=x, y=y, hue=hue)
        plt.title(titulo if titulo else f'{y} vs {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def boxplot(self, datos, columna, titulo=None):
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=datos, y=columna)
        plt.title(titulo if titulo else f'Distribución de {columna}')
        plt.ylabel(columna)
        plt.show()
