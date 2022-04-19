<h1 align="center">Serie de notas</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/Serie_de_Notas) queda resuelto el ejercicio de serie de datos. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Ejercicio 1

Vamos a utilizar un caso práctico que se usa muchas veces en la presentación de las nociones básicas de estadísticas: la descripción y el análisis de una serie de notas que ha obtenido un estudiante. Este caso práctico es sencillo y todo el mundo se siente implicado porque se basa en nuestra experiencia. Además, nos permitirá entender las nociones necesarias para la comprensión de datos que también son aplicables a los casos más complejos que vamos a tratar en los capítulos siguientes.

Este es el contexto: actualmente está en formación para convertirse en experto en inteligencia artificial y acaban de darle sus notas trimestrales, que puede ver a continuación (se trata de una puntuación sobre 20): [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]

Como puede comprobar, esta pequeña serie estadística contiene muchas notas distintas. Primero vamos a proceder a la deducción de una tendencia central, es decir, intentar determinar un valor alrededor del que se concentra el conjunto de las notas. Luego estudiaremos su dispersión y al final buscaremos la existencia de datos aberrantes, es decir, no representativos del conjunto de las notas. Todos recordamos un examen donde no habíamos repasado los conceptos principales y obtuvimos una nota no representativa de las notas que habíamos obtenido durante el año.

Debe realizar este tipo de análisis en cualquier serie de observaciones que tendrá que utilizar en el ámbito de los proyectos de Machine Learning. En efecto, hacer mediciones de tendencia y de dispersión de sus datos le permitirá comprender su significado, su papel y su utilidad en la predicción que se ha de efectuar. Identificar los datos aberrantes le permitirá excluir datos no representativos que podrían alterar el aprendizaje.


El código empleado para resolverlo es el siguiente: 

```python
import matplotlib.pyplot as plt

class Serie_notas:
    def __init__ (self, notas, suma_notas, media, moda, dato_max, dato_min, x1, x2, x3, y1, y2, y3):
        self.notas = notas
        self.suma_notas = suma_notas ; self.media = media
        self.moda = moda ; self.dato_max = dato_max
        self.dato_min = dato_min ; self.x1 = x1
        self.x2 = x2 ; self.x3 = x3 ; self.y1 = y1
        self.y2 = y2 ; self.y3 = y3
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
        x1 = [1,2] ; x2 = [6,9,10,11,12,14] ; x3 = [3,4,5,7,8,13,15,16]
        y1 = [3,19] ; y2 = [11,11,11,12,12,12] ; y3 = [10,15,14,9,8,13,14,16]
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
    def datos_aberrantes():
        notas = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
        dato_max = max(notas) ; dato_min = min(notas)
        print(f"\nLos datos aberrantes son {dato_max} and {dato_min}")

def iniciar():
    Nota = Serie_notas
    Nota.calcular_media()
    Nota.calcular_moda()
    Nota.datos_aberrantes()
    Nota.grafico_dispersion()
    Nota.diagrama_cajas()
    Nota.diagrama_violin()
```

Su UML:


En formato [XML]()
