import matplotlib


import matplotlib.pyplot
Notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
suma_notas = 0
for i in range (len(Notas)):
    nota = Notas.pop(0)
    suma_notas += nota
print(suma_notas)