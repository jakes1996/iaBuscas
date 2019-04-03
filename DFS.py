class Vertice:
    def __init__(self, nome):
        self.id = nome
        self.adjacentes = {}
        self.descoberto = 0
        self.terminado = 0
        self.cor = 'preto'

    def __str__(self):
        return 'Vertice: ' + self.id + ' | Vizinhos: ' + str([x.id for x in self.adjacentes])

    def addVizinho(self, vizinho, distancia=0):
        self.adjacentes[vizinho] = distancia

    def getArestas(self):
        return self.adjacentes.keys()  

    def getVerticeId(self):
        return self.id

    def getDistancia(self, vizinho):
        return self.adjacentes[vizinho]

class Graph:
    
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        self.tempo = 1

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        string = ''
        for key in sorted(list(self.vertices.keys())):
            string += ' %s' %(self.vertices[key]) + ' | Descoberto: ' + str(self.vertices[key].descoberto) + ' | Terminado: ' + str(self.vertices[key].terminado) + '|  Cor: ' +  str(self.vertices[key].cor) + '\n'
        return string

    def addVertice(self, v):
        self.num_vertices = self.num_vertices + 1
        novoVertice = Vertice(v)
        self.vertices[v] = novoVertice
        return novoVertice

    def getVertice(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def addAresta(self, u, v, distancia = 0):
        if u not in self.vertices:
            self.addVertice(u)
        if v not in self.vertices:
            self.addVertice(v)

        self.vertices[u].addVizinho(self.vertices[v], distancia)
        self.vertices[v].addVizinho(self.vertices[u], distancia)

    def getVertices(self):
        return self.vertices.keys()

    def _buscaProfundidade(self, vertice):
        self.vertices[vertice].cor = 'vermelho'
        self.vertices[vertice].descoberto = self.tempo
        self.tempo += 1
        for vizinho in self.vertices[vertice].adjacentes:
            if self.vertices[vizinho.id].cor == 'preto':
                self._buscaProfundidade(vizinho.id)
        self.vertices[vertice].cor = 'azul'
        self.vertices[vertice].terminado = self.tempo
        self.tempo += 1

    def buscaProfundidade(self, vertice):
        self._buscaProfundidade(vertice)


if __name__ == '__main__':

    grafo = Graph()

    grafo.addVertice('Arad')
    grafo.addVertice('Zerind')
    grafo.addVertice('Oradea')
    grafo.addVertice('Sibiu')
    grafo.addVertice('Rimnicu Vilcea')
    grafo.addVertice('Timisoara')
    grafo.addVertice('Mehadia')
    grafo.addVertice('Dobreta')
    grafo.addVertice('Craiova')
    grafo.addVertice('Pitesti')
    grafo.addVertice('Fagaras')
    grafo.addVertice('Giurgiu')
    grafo.addVertice('Bucharest')
    grafo.addVertice('Urziceni')
    grafo.addVertice('Eforie')
    grafo.addVertice('Hirsova')
    grafo.addVertice('Vaslui')
    grafo.addVertice('Iasi')
    grafo.addVertice('Neamt') 


    grafo.addAresta('Arad','Zerind',75)
    grafo.addAresta('Arad','Sibiu',140)
    grafo.addAresta('Arad','Timisoara',118)
    grafo.addAresta('Zerind','Oradea',71)
    grafo.addAresta('Sibiu','Oradea',151)
    grafo.addAresta('Sibiu','Fagaras',99)
    grafo.addAresta('Sibiu','Rimnicu Vilcea',80)
    grafo.addAresta('Pitesti','Rimnicu Vilcea',97)
    grafo.addAresta('Craiova','Rimnicu Vilcea',146)
    grafo.addAresta('Lugoj','Timisoara',111)
    grafo.addAresta('Lugoj','Mehadia',70)
    grafo.addAresta('Dobreta','Mehadia',75)
    grafo.addAresta('Dobreta','Craiova',120)
    grafo.addAresta('Pitesti','Craiova',138)
    grafo.addAresta('Pitesti','Bucharest',101)
    grafo.addAresta('Bucharest','Fagaras',211)
    grafo.addAresta('Giurgiu','Bucharest',90)
    grafo.addAresta('Urziceni','Bucharest',85)
    grafo.addAresta('Urziceni','Hirsova',98)
    grafo.addAresta('Urziceni','Vaslui',142)
    grafo.addAresta('Eforie','Hirsova',86)
    grafo.addAresta('Iasi','Vaslui',92)
    grafo.addAresta('Iasi','Neamt',87)

    grafo.buscaProfundidade('Arad')
    print(grafo)
