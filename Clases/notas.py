import matplotlib


import matplotlib.pyplot

class Serie_notas:
    def __init__ (self, notas, suma_notas):
        self.notas = notas
        self.suma_notas = suma_notas
    def tendencia_central():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        suma_notas = 0
        for i in range (len(notas)):
            nota = notas.pop(0)
            suma_notas += nota
        print(suma_notas)
Serie_notas.tendencia_central()