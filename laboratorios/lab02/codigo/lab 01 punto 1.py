from itertools import permutations
from collections import deque
from cmath import inf

class GraphAL:
    def init(self, size):
        self.size=size
        self.arregloDeListas = [0]*size # = [0,0,0,0...]
        for i in range(size):
            self.arregloDeListas[i] = deque()

    def addArc(self, source, destination, weight):
        laListaLlegada = self.arregloDeListas[source]
        unaPareja = (destination,weight)
        laListaLlegada.append(unaPareja)

    def getWeight(self, source, destination):
        laListaLlegada = self.arregloDeListas[source]
        if destination not in self.getSuccessors(source):
            return inf
        for i in range(len(laListaLlegada)):
            pareja = laListaLlegada[i] # O(n)
            theDestination = pareja[0]
            theWeight = pareja[1]
            if theDestination == destination:
                return theWeight
        for (theDestination,theWeight) in laListaLlegada:
            if theDestination == destination:
                return theWeight
        return 0
    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for (theDestination,theWeight) in laListaLlegada:
            otraListica.append(theDestination) 
        return otraListica
def recorridos(grafo):
    lista = []
    visitado=[False]*grafo.size
    for i in range(grafo.size):
        if not visitado[i]:
            visitado[i]=True
            lista.append(i)
            for sucesor in grafo.getSuccessors(i):
                if not visitado[i]:
                    visitado[sucesor]=True
                    lista.append(i)
    return lista


def permutaciones(grafo,perm):
    perm1 = permutations(perm)
    for i in list(perm1):
        print
        print (i)
    perm1 = permutations(perm)
    pesoT = inf
    for i in list(perm1):
        peso = 0
        count = 0
        for j in i:
            count = count + 1 
            if j != i[-1]:
                peso += grafo.getWeight(j,i[count])
            else :
                peso += grafo.getWeight(j,i[0])
                print(peso)
                if peso < pesoT:
                    pesoT = peso
    print("este es el menor peso: " + str(pesoT) ) 

def main():
    grafo=GraphAL(3)
    grafo.addArc(0,0,4) 
    grafo.addArc(0,1,8) 
    grafo.addArc(0,2,3) 
    grafo.addArc(1,0,1) 
    grafo.addArc(1,1,7) 
    grafo.addArc(1,2,3)
    grafo.addArc(2,0,6) 
    grafo.addArc(2,1,2)
    grafo.addArc(2,2,5)
    lista = recorridos(grafo)
    permutaciones(grafo,lista)
main()