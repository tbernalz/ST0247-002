import numpy as np

class Grafo:


    def __init__(self, nodos):

        self.matriz = np.zeros((nodos,nodos))

        self.colores = [None]*nodos

        self.colores[0] = True


    def color(self):

        for i in range(len(self.matriz)):

            x = not self.colores[i]

            for j in range(len(self.matriz)):

                if self.matriz[i][j] !=0:

                    if  self.colores[j]!= None and self.colores[j]!= x:

                        print("No es bicoloreable")

                        return 
                    else:

                        self.colores[j] = x
        
        print("Si es coloreable")


    def Arcos(self,sta,end):

        self.matriz[sta][end] = 1
        self.matriz[end][sta] = 1


def main():

    nodos = int(input())

    while nodos != 0:
        arcos = int(input())
        grafo = Grafo(nodos)

        for i in range(arcos):

            arco = list(map(int, input().split()))
            grafo.Arcos(arco[0],arco[1])

        grafo.color()
        nodos = int(input())
main()