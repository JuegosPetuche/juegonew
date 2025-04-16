import numpy as np
from Neurona import Neuron

class Capa:

    def __init__(self, numNeuronas, numEntrada):
        self.neuronas = [Neuron(numEntrada) for _ in range(numNeuronas)]

    def adelante(self, entrada):
        salida = np.array([neurona.adelante(entrada) for neurona in self.neuronas])
        return salida
    
    
    def atras(self, derivadaSalida, tazaAprendizaje):
        derivadaEntrada = np.zeros(len(self.neuronas[0].entrada))

        for i, neuron in enumerate(self.neuronas):
            derivadaEntrada += neuron.atras(derivadaSalida[i], tazaAprendizaje)

        return derivadaEntrada
