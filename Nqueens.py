
class NRainhas:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.colunas = []
 
    def inserirNaProxColuna(self, coluna):
        self.colunas.append(coluna)
 
    def removerDaColunaAtual(self):
        return self.colunas.pop()
 
    def verificaProximaColuna(self, coluna):
        linha = len(self.colunas)
        # verifica coluna
        for rainha in self.colunas:
            if coluna == rainha:
                return False
        # verifica diagonal
        for linhaDaRainha, colunaDaRainha in enumerate(self.colunas):
            if colunaDaRainha - linhaDaRainha == coluna - linha:
                return False
 
        # verifica outra diagonal
        for linhaDaRainha, colunaDaRainha in enumerate(self.colunas):
            if ((self.tamanho - colunaDaRainha) - linhaDaRainha == (self.tamanho - coluna) - linha):
                return False
        return True
 
    def printarTabuleiro(self):
        print(self.colunas)
 
 
def solucaoComBuscaGulosa(tamanho):
    tabuleiro = NRainhas(tamanho)
    quantSolucoes = 0
    linha = 0
    coluna = 0
    solucaoEncontrada = False

    while True:
        # place queen in next row
        while coluna < tamanho:
            if tabuleiro.verificaProximaColuna(coluna):
                tabuleiro.inserirNaProxColuna(coluna)
                linha += 1
                coluna = 0
                break
            else:
                coluna += 1
 
        # if could not find column to place in or if board is full
        if (coluna == tamanho or linha == tamanho):
            # se o tabuleiro está cheio, então temos uma solução
            if linha == tamanho:
                tabuleiro.printarTabuleiro()
                quantSolucoes += 1
                tabuleiro.removerDaColunaAtual()
                linha -= 1
                solucaoEncontrada = True

            try:
                if solucaoEncontrada:
                    break
                else:
                    colunaAnterior = tabuleiro.removerDaColunaAtual()
            except IndexError:
                # all queens removed
                # thus no more possible configurations
                break
            # try previous row again
            linha -= 1
            # start checking at column = (1 + value of column in previous row)
            coluna = 1 + colunaAnterior
 
 
n = int(input('Tamanho do tabuleiro (n): '))
solucaoComBuscaGulosa(n)