import numpy as np

class Neuron:

    def __init__(self, nInput):

        self.peso = np.random.randn(nInput)
        self.bias = np.random.randn()
        self.salida = 0
        self.entrada = None
        self.derivadaPeso = np.zeros_like(self.peso)
        self.derivadaBias = 0

    def activar(self, x):

        return 1 / (1 + np.exp(-x))
    
    def derivada_activar(self, x):

        return x * (1 - x)
    
    def adelante(self, entrada):

        self.entrada = entrada
        sumaPonderada = np.dot(entrada, self.peso) + self.bias
        self.salida = self.activar(sumaPonderada)

        return self.salida
    
    def atras(self, derivadaSalida, tazaAprendizaje):

        derivadaActivacion = derivadaSalida * self.derivada_activar(self.salida)
        self.derivadaPeso = np.dot(self.entrada, derivadaActivacion)
        self.derivadaBias = derivadaActivacion
        derivadaEntrada = np.dot(derivadaActivacion, self.peso)
        self.peso -= self.derivadaPeso * tazaAprendizaje
        self.bias -= tazaAprendizaje * self.derivadaBias

        return derivadaEntrada
