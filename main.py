import pandas as pnd
import Clases_Rubén.JMPEstadisticas as jmp
import numpy as np

from Clases import notas
if __name__ == '__main__':
    eleccion = int(input(("¿Qué versión quieres usar? \n 1: La creada anterior a las nuevas pautas \n 2: La nueva dada por las nuevas pautas\n")))
    if eleccion == 1:
        notas.iniciar()
    elif eleccion ==2:
        datos = pnd.read_csv("Student_grade.csv", header=0 , sep =",")
        lista_notas = list(datos["Notas"])
        # observaciones = pnd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})
        stats = jmp.JMPEstadisticas(lista_notas)
        stats.analisisCaracteristica()
