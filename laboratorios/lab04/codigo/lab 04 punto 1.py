from cmath import inf
from collections import deque

class GraphAL:
    def __init__(self, size):
        self.size=size
        self.arregloDeListas = [0]*size # = [0,0,0,0...]     
        
        for i in range(size):
            self.arregloDeListas[i] = deque()
            
            
    def addArc(self, source, destination, weight):
        laListaLlegada = self.arregloDeListas[source]
        unaPareja = (destination,weight)
        laListaLlegada.append(unaPareja)
        
        
    def getWeight(self, source, destination):
        if destination not in self.getSuccessors(source):
            return inf
        laListaLlegada = self.arregloDeListas[source]
        
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
    
    
def voraz(grafo,cercano,n,pesoMenor,lista,visitados):
    visitados[cercano] = 1
    menor = inf
    if cercano == n:
        visitados[cercano] = 0
        lista.append(cercano)
        return lista,pesoMenor
    else:
        for sucesor in grafo.getSuccessors(cercano):
            peso = grafo.getWeight(cercano,sucesor)
            if peso<menor and not visitados[sucesor]:
                menor = peso
        pesoMenor+=menor
        lista.append(cercano)
        l,p = voraz(grafo, sucesor, n, pesoMenor,lista,visitados)
    visitados[cercano] = 0
    return lista,p


def main():
    p = list(input())
    n = int(p[0])
    m = int(p[2])
    g = GraphAL(n+1)
    visitados= [0]*(n+1)
    
    for i in  range(0,m):
        entrada = list(input())
        a = int(entrada[0])
        b = int(entrada[2])
        c = int(entrada[4])
        g.addArc(a, b, c)
    print(voraz(g,1,n,0,[],visitados))
    
    
main()