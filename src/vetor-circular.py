class vetorCircular:
    def __init__(self, k):
        self.tamMax = k
        self.tamAtual = 0
        self.vector = [""] * k
        self.posInicial = -1
        self.posFinal = -1

    def adicionaVetor(self, value):
        if self.isFull():
            print('está cheio impossível adicionar: ', value)
            return False
        
        posFinal = (self.posFinal+1) % self.tamMax
        self.vector[posFinal] = value
        self.posFinal = posFinal
        self.tamAtual += 1
        if self.tamAtual == 1:
            self.posInicial = 0

        return True

    def removeVetor(self):
        if self.isEmpty():
            print('está vazio')
            return False
        
        self.posInicial = (self.posInicial+1) % self.tamMax
        self.tamAtual -= 1
        if self.isEmpty():
            self.posInicial = -1
            self.posFinal = -1
                
        return True
        
    def inicioVetor(self):
        if self.isEmpty():
            return -1
        
        return self.vector[self.posInicial]

    def fimVetor(self):
        if self.isEmpty():
            return -1
        
        return self.vector[self.posFinal]

    def isEmpty(self):
        return self.tamAtual == 0

    def isFull(self):
        return self.tamAtual == self.tamMax
    
    def exibeVetorCircular(self):
        if(self.posInicial == -1):
            print("Sem Elementos no Vetor")

        elif (self.posFinal >= self.posInicial):
            for i in range(self.posInicial, self.posFinal + 1):
                print(self.vector[i], end=" ")
            print()
        else:
            for i in range(self.posInicial, self.tamMax):
                print(self.vector[i], end=" ")
            for i in range(0, self.posFinal + 1):
                print(self.vector[i], end=" ")
            print()


vetorC = vetorCircular(5)
vetorC.adicionaVetor(1)
vetorC.adicionaVetor(2)
vetorC.adicionaVetor(3)
vetorC.adicionaVetor(4)
vetorC.adicionaVetor(5)
vetorC.removeVetor()
vetorC.removeVetor()
vetorC.adicionaVetor(0)
vetorC.adicionaVetor(9)



vetorC.exibeVetorCircular()

    
    # https://leetcode.com/problems/design-circular-queue/ - baseado na resolução da seguinte questão do leetcode

    # vetorCircular(k): Construtor de um vetor circular .
    # inicioVetor: Retorna o início do vetor, se ele estiver vazio, exibe na tela essa informação e retorna -1
    # fimVetor: Retorna o fim do vetor, se ele estiver vazio, exibe na tela essa informação e retorna -1
    # adicionaVetor(value): Insere um novo elemento no vetor e retorna true se a operação foi completada
    # removeVetor(): remove um elemento no vetor e retorna true se a operação foi completada
    # isEmpty(): Checa se o vetor está vazio ou não.
    # isFull(): Checa se o vetor está cheio ou não.
    # exibeVetorCircular() : Exibe o vetor circular em tela
