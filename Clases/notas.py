import matplotlib.pyplot as plt
import numpy as np

class Serie_notas:
    def __init__ (self, notas, suma_notas, media, moda, dato_max, dato_min):
        self.notas = notas
        self.suma_notas = suma_notas
        self.media = media
        self.moda = moda
        self.dato_max = dato_max
        self.dato_min = dato_min
    def media():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        suma_notas = 0
        for i in range (len(notas)):
            nota = notas.pop(0)
            suma_notas += nota
        media = suma_notas / 20
        print(f"La media de las notas es {media}")
    def moda():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        notas.sort() ; print(notas)
        moda = max(set(notas), key = notas.count)
        print(f"La tendencia central de las notas es {moda}")
    def dispersion():
        x = np.random.randint (1,16, size= 16)
        y = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        plt.scatter(x,y) ; plt.show()
    def datos_aberrantes():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        dato_max = max(notas) ; dato_min = min(notas)
        print(f"Los datos aberrantes son {dato_max} and {dato_min}")

Serie_notas.media()
Serie_notas.moda()
Serie_notas.dispersion()
Serie_notas.datos_aberrantes()