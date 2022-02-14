import pandas as pd
from IPython.display import display
import json


dictionary1 = {}
dictionary2 = {}


file1 = open("textoPrueba.txt")



for line in file1:
    
    ID, x, y, nombre = line.split(" ")    
    # print ("id:" , ID," | x:" , x," | y:" , y," | nombre:" + nombre )    
    dictionary1[nombre.replace("\n", "")] = ID, x, y, nombre.replace("\n", "")
    
file1.close()
    
   
# print(dictionary1, "\n", "\n")
print(json.dumps(dictionary1, sort_keys=False, indent=4))
df1 = pd.DataFrame(dictionary1)
display(df1)


print ("FIN dictionary1" , "\n", "\n")

###############################################################################

file2 = open("textoPrueba2.txt")

contador = 1

for line in file2:
    
    if len(line.split()) == 5:
        ID1, ID2, distancia, nombre, nombre1 = line.split(" ")
        nombre = (nombre+nombre1).replace(" ", "")
        
    else:        
        ID1, ID2, distancia, nombre = line.split(" ")
    
    # print ("id1:" , ID1,"id2:" , ID2," | distancia:" , distancia," | nombre:" + nombre )    
    
    dictionary2[contador] = ID1, ID2, distancia, nombre.replace("\n", "")
    contador+=1
    
file2.close()
    
    
# print(dictionary2, "\n", "\n")
print(json.dumps(dictionary2, sort_keys=False, indent=4))

# df1 = pd.DataFrame(dictionary2)
# display(df1)










