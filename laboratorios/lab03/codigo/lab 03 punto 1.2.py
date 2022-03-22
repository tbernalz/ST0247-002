def seAtacanHastaI(tablero, i):
    for j in range(0, i+1):
        for k in range(j+1, i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j] == tablero[k]:
                return True
    return False


def nReinas(n:int) -> None:
    print(nReinasAux(n, 0, [0]*n, []))
    

def nReinasAux(n:int, col:int, lista:list, primero:list) -> None:
    if col == n:
        primero.append(lista.copy())
        return 
    else:
        for f in range(n):
            lista[col] = f
            if seAtacanHastaI(lista, col):
                pass
            else:
                nReinasAux(n, col+1, lista, primero)
            if primero == []:
                pass
            else:
                return primero
            


def main():
    nReinas(4)


main()