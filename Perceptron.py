import math

#o perceptron com a função de ativação sigmoidiana
class Perceptron:

    def __init__(self, entradas, pesos,  bias):
        self.entradas = entradas # todas as entradas
        self.pesos = pesos # vetor dos pesos        
        self.bias = bias # bias
        #self.saidas = saidas # saídas respectivas de cada entradas
        #self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
        #self.epocas = epocas # número de épocas
        #self.num_entradas = len(entradas) # quantidade de entradas
        #self.num_entradas = len(entradas[0]) # quantidade de elementos por cada entra
        
    #somatório
    def somatorio(self):
        result = self.bias
        for i in range(len(self.entradas)):
            result += self.entradas[i] * self.pesos[i]
        return result

    #função sigmoidiana
    def sigmoide(self, somatorio):
        return 1 / (1 + math.exp(-somatorio))