import matplotlib.pyplot as plt
class Serie_notas:
    def __init__ (self, notas, suma_notas, media, moda, dato_max, dato_min, x):
        self.notas = notas
        self.suma_notas = suma_notas ; self.media = media
        self.moda = moda ; self.dato_max = dato_max
        self.dato_min = dato_min ; self.x = x
    def calcular_media():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        suma_notas = 0
        for i in range (len(notas)):
            nota = notas.pop(0)
            suma_notas += nota
        media = suma_notas / 20
        print(f"\nLa media de las notas es {media}\n")
    def calcular_moda():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        notas.sort() ; moda = max(set(notas), key = notas.count)
        print(f"\nLa tendencia central de las notas es {moda}\n")
    def datos_aberrantes():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        dato_max = max(notas) ; dato_min = min(notas)
        print(f"\nLos datos aberrantes son {dato_max} and {dato_min}\n")
    def graficos():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16] ; notas.sort()
        y = notas
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        colores = ["r", "b", "b", "b", "g", "g", "g", "g", "g", "g", "b", "b", "b", "b", "b", "r"]
        plt.subplot(2, 2, 1)
        plt.scatter(x,y ,color = colores)
        plt.title("Gráfico de dispersión")
        plt.subplot(2, 2, 2)
        plt.boxplot([[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]])
        plt.title("Diagrama de cajas")
        plt.subplot(2,2,3)
        plt.violinplot([[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]])
        plt.title("Diagrama de violín")
        plt.show()
def iniciar():
    Nota = Serie_notas
    Nota.calcular_media()
    Nota.calcular_moda()
    Nota.datos_aberrantes()
    Nota.graficos()
