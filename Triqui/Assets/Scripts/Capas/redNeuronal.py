import numpy as np

from Capas import Capa

class redNeuronal:

    def __init__(self):
        
        self.capas = []
        self.listaPerdida = []

    def añadirCapa(self, numNeurona, numEntrada):
        if not self.capas:
            self.capas.append(Capa(numNeurona, numEntrada))
        else:
            tamañoSalidaPrevia = len(self.capas[-1].neuronas)
            self.capas.append(Capa(numNeurona, tamañoSalidaPrevia))

    def adelante(self, entradas):
        for capa in self.capas:
            entradas = capa.adelante(entradas)
        return entradas
    
    def atras(self, gradientePerdida, tazaAprendizaje):
        for capa in reversed(self.capas):
            gradientePerdida = capa.atras(gradientePerdida, tazaAprendizaje)

    def entrenar(self, x, y, epocas=1000, tazaAprendizaje=0.01):
        for epoca in range(epocas):
            perdida = 0
            for i in range(len(x)):
                salida = self.adelante(x[i])
                perdida += np.mean((y[i] - salida) ** 2)
                gradientePerdida = 2 * (salida - y[i])
                self.atras(gradientePerdida, tazaAprendizaje)
            perdida /= len(x)
            self.listaPerdida.append(perdida)

            if epoca % 100 == 0:
                print(f"Epoca: {epoca}, peridida: {perdida}")

    def predecir(self, x):
        predicciones = []
        for i in range(len(x)):
            predicciones.append(self.adelante(x[i]))
        return np.array(predicciones)
    
x = np.array([[0.5, 0.2, 0.1], 
              [0.9, 0.7, 0.3], 
              [0.3, 0.6, 0.9]])

y = np.array([[0.3], [0.6], [0.9]])

rN = redNeuronal()

rN.añadirCapa(numNeurona=3, numEntrada=3)
rN.añadirCapa(numNeurona=3, numEntrada=3)
rN.añadirCapa(numNeurona=1, numEntrada=3)

rN.entrenar(x, y, epocas=25300, tazaAprendizaje=0.1)

print(f"Prediccion: {rN.predecir(x)}")

