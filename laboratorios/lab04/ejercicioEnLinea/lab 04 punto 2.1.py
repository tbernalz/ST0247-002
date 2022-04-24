def main():
  stack = []
  temp = ""
  
  while (temp != "0 0 0"):
    temp = str(input())
    stack.append(temp) 
    if (temp == "0 0 0"):
      stack.pop()
      
  while stack:
    temp2 = ""
    temp3 = ""
    count2 = 0
    temp1 = 0
    cont = 0
    valor = 0
    stack2 = []
    stack3 = []
    p = (stack.pop(0))
    
    for i in  p:
      if(i == " "):
        stack2.append(temp2)
        temp2=""
      else:
        temp2+=i
    r = int(stack2.pop())
    d = int(stack2.pop())
    n = int(stack2.pop())
    
    for j in range(0,n):
      o = (stack.pop(0))
      for i in  o:
        if(i == " "):
          cont = cont + 1
          stack3.append(temp3)
          temp3=""
        else:
          temp3+=i
          
    for i in range(0,cont+n):
      if(count2 == 2):
        if(temp1 > d):
          extra = temp1 - d
          valor =  valor + (r * extra) 
        temp1 = 0
        count2 = 0
      else:
        temp1 = temp1 + int(stack3.pop())
        count2 = count2 + 1
    print(valor)
    
    
main()