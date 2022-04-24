import numpy as np


def lcsDP(A,B): #Corregido
    m,n = (len(A)+1), (len(B)+1)
    tabla = np.zeros((m,n))
    
    for i in range (0,n): ## condicion de parada 
      tabla[0][i] = 0
      
    for j in range (0,m): ## condicion de parada 
      tabla[j][0] = 0
      
    for i in range(1,m): ## recursividad
      for j in range(1,n):
        if A[i-1] == B[j-1]:                
          tabla[i][j] = 1 + tabla[i-1][j-1]
        else:
          tabla[i][j] = max(tabla[i-1][j], tabla[i][j-1])
    print (tabla)
    return tabla[m-1][n-1]


def main():
  print(lcsDP("abdace","babce"))
  
  
main()