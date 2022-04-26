import matplotlib.pyplot as plt ; import pandas as pnd

class Serie_notas:
    global datos , lista_notas
    datos = pnd.read_csv("Student_grade.csv", header=0 , sep =",")
    lista_notas = list(datos["Notas"])
    def __init__ (self, notas, suma_notas, media, moda, dato_max, dato_min, x):
        self.notas = notas
        self.suma_notas = suma_notas ; self.media = media
        self.moda = moda ; self.dato_max = dato_max
        self.dato_min = dato_min ; self.x = x
    def calcular_media():
        suma_notas = 0 ; total = len(lista_notas)
        for i in range (len(lista_notas)):
            nota = lista_notas.pop(0)
            suma_notas += nota
        media = suma_notas / total
        print(f"\nLa media de las notas es {media}\n")
    def calcular_moda():
        datos = pnd.read_csv("Student_grade.csv", header=0 , sep =",")
        lista_notas = list(datos["Notas"])
        lista_notas.sort() ; moda = max(set(lista_notas), key = lista_notas.count)
        print(f"\nLa tendencia central de las notas es {moda}\n")
    def datos_aberrantes():
        datos = pnd.read_csv("Student_grade.csv", header=0 , sep =",")
        lista_notas = list(datos["Notas"])
        dato_max = max(lista_notas) ; dato_min = min(lista_notas)
        print(f"\nLos datos aberrantes son {dato_max} and {dato_min}\n")
    def graficos():
        datos = pnd.read_csv("Student_grade.csv", header=0 , sep =",")
        lista_notas = list(datos["Notas"]) ; lista_notas.sort()
        x = [1,2,3,4,5,6,7,8,9,10]
        plt.subplot(2, 2, 1)
        plt.scatter(x,lista_notas ,color = "green")
        plt.title("Gráfico de dispersión")
        plt.subplot(2, 2, 2)
        plt.boxplot(lista_notas)
        plt.title("Diagrama de cajas")
        plt.subplot(2,2,3)
        plt.violinplot(lista_notas)
        plt.title("Diagrama de violín")
        plt.show()

def iniciar():
    Nota = Serie_notas
    Nota.calcular_media()
    Nota.calcular_moda()
    Nota.datos_aberrantes()
    Nota.graficos()
