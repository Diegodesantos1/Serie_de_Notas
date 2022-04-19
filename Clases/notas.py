import matplotlib.pyplot as plt

class Serie_notas:
    def __init__ (self, notas, suma_notas, media, moda, dato_max, dato_min, x1, x2, x3, y1, y2, y3):
        self.notas = notas
        self.suma_notas = suma_notas
        self.media = media
        self.moda = moda
        self.dato_max = dato_max
        self.dato_min = dato_min
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
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
    def grafico_dispersion():
        x1 = [1,2] ; x2 = [6,9,10,11,12,14] ; x3 = [3,4,5,7,8,13,15,16] #colocados por posición
        y1 = [3,19] ; y2 = [11,11,11,12,12,12] ; y3 = [10,15,14,9,8,13,14,16] #colocado por notas
        plt.scatter(x1,y1, color = "red" ,label="Datos aberrantes")
        plt.scatter(x2,y2, color = "green" ,label="Tendencia Central")
        plt.scatter(x3,y3, color = "blue" ,label="Resto")
        plt.legend() ; plt.title("Gráfico de dispersión"); plt.show()
    def diagrama_cajas():
        plt.boxplot([[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]])
        plt.title("Diagrama de cajas") ; plt.show()
    def diagrama_violin():
        plt.violinplot([[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]])
        plt.title("Diagrama de violín") ; plt.show()

def iniciar():
    Nota = Serie_notas
    Nota.calcular_media()
    Nota.calcular_moda()
    Nota.datos_aberrantes()
    Nota.grafico_dispersion()
    Nota.diagrama_cajas()
    Nota.diagrama_violin()