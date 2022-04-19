import matplotlib.pyplot as plt
import numpy as np

class Serie_notas:
    global notas
    notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
    def __init__ (self, notas, suma_notas):
        self.notas = notas
        self.suma_notas = suma_notas
    def media():
        suma_notas = 0
        for i in range (len(notas)):
            nota = notas.pop(0)
            suma_notas += nota
        media = suma_notas / 20
        print(f"La tendencia central de las notas es {media}")
    def moda():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        notas.sort() ; print(notas)
        moda = max(set(notas), key = notas.count)
        print(f"la moda es {moda}")
    def dispersion():
        x = np.random.randint (1,16, size= 16)
        y = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        plt.scatter(x,y) ; plt.show()

Serie_notas.media()
Serie_notas.moda()
Serie_notas.dispersion()