def seAtacanHastaI(tablero, i):
    for j in range(0, i+1):
        for k in range(j+1, i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j] == tablero[k]:
                return True
    return False


def nReinas(n:int):
    lista = nReinasAUX(n,0,[0]*n,tablero(n),[])
    return lista
        

def nReinasAUX(n:int, c:int, l:list, m, lista1:list):
    if c == n:
        lista1.append(l)
        return
    else:
        for f in range(n):
            if m[c][f] == True:
                l[c] = f
            else:
                pass
            if seAtacanHastaI(l,c):
                pass
            else:
                nReinasAUX(n,c+1,l,m,lista1)
    return len(lista1)


def tablero(n):
    lista2 = []
    for i in range(n):
        print ("Digite la fila del tablero (faltan " + str(n-i) + ")")
        linea = input()
        listPeque = []
        for letra in linea:
            if letra == '.':
                listPeque.append(True)
            elif letra == '*':
                listPeque.append(False)
        lista2.append(listPeque)
    return lista2
    
    
    
    
    
def main ():
    contador = 1
    casosPosibles = 0
    respuestas = []
    while contador == 1:
        print ("Digite el número de reinas")
        n = int(input())
        if n == 0:
            contador = 0
        else:
            respuestas.append(nReinas(n))
            casosPosibles += 1     
        print()
    for i in range(casosPosibles):
        print("Case " + str(contador+1) + ": " + str(respuestas[i]))
        
        
        
        
main()
    
    
    
    
