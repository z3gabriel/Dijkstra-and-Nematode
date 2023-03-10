class Grafo:
    def __init__(self, vertices):
        self.v = vertices
        self.grafo = [[0 for x in range(vertices)]
                      for y in range(vertices)]

    def adiciona_araesta(self, u, v, p):
        self.grafo[u][v] = p

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.v):
            print(self.grafo[i])

    def minDist(self, dist, relaxar):
        min = 999999999999
        ind = -1

        for j in range(self.v):
            if dist[j] < min and j in relaxar:
                ind = j
                min = dist[j]

        if ind == -1:
            return None
        else:
            return ind

    def printCaminho(self, antecessor, j):
        aux = []
        continua = True
        while continua:
            if antecessor[j] != -1:
                aux.append(j)
                j = antecessor[j]
            else:
                aux.append(j)
                continua = False

        aux2 = aux[::-1]
        for j in aux2:
            print(j, end=' ')

        return aux2

    def resposta(self, origem, dist, antecessor, destino):
        i = destino
        if dist[i] == 999999999999:
            print(f'\nNão há um caminho entre {origem} e {destino}')
        else:
            print(f'\nA distância entre {origem} e {destino} é de {dist[i]}', end='\n')
            print('O caminho é: ', end=' ')
            res = self.printCaminho(antecessor, i)
            fplot(res)

    def dijkstra(self, origem, destino):
        dist = [999999999999] * self.v
        dist[origem] = 0
        antecessor = [-1] * self.v
        relaxar = []

        for i in range(self.v):
            relaxar.append(i)

        fim = False
        while not fim:
            u = self.minDist(dist, relaxar)

            if u is not None:
                relaxar.remove(u)

                for i in range(self.v):
                    if self.grafo[u][i] and i in relaxar:
                        if dist[u] + self.grafo[u][i] < dist[i]:
                            dist[i] = dist[u] + self.grafo[u][i]
                            antecessor[i] = u
            else:
                fim = True

        self.resposta(origem, dist, antecessor, destino)

from igraph import *
def fplot(lista):
    f = Graph(directed=True)
    cont = 0
    conexoes = []

    for count in range(len(lista)-1):
        conexoes.append((cont, cont+1))
        cont += 1

    f.add_vertices(len(lista))
    f.add_edges(conexoes)
    vertices = []
    ed = lista
    for x in ed:
        vertices.append(x)

    visual_style = {}
    visual_style['vertex_size'] = 35
    visual_style['vertex_label'] = vertices
    visual_style['vertex_color'] = 'red'
    plot(f,**visual_style)

qtdVertices = 0
with open('teste3.txt', 'r') as arquivo:
    for x in arquivo:
        x = x.split(' ')
        if 'id' in x:
            qtdVertices += 1

g = Grafo(qtdVertices)
cont = 0
with open('teste3.txt', 'r') as arquivo:
    for x in arquivo:
        x = x.split(' ')
        if 'source' in x:
            u = int(x[-1])
            cont += 1
        if 'target' in x:
            v = int(x[-1])
            cont += 1
        if 'value' in x:
            p = int(x[-1])
            cont += 1
        if cont == 3:
            g.adiciona_araesta(u, v, p)
            cont = 0

origem = int(input('Digite o vértice de origem (número inteiro) entre 0 e 296: '))
destino = int(input('Digite o vértice de destino (número inteiro) entre 0 e 296: '))

g.dijkstra(origem, destino)
