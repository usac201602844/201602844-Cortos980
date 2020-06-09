numero =488
lista=[]
lista1=[]
numero1=0
numero2=0
listadesecuencia=[numero]

##################funcion de collatz
def collat(n):
    n1=0
    #verificamos si es par
    if n%2 ==0:
        n1 == n//2
    else:
        n1 == 3*n+1
    return n1

###################Contrar la sucecion de numero 488 - 88 - 8
for j in str(numero):
    lista.append(j)
#print(lista)

if len(str(numero))>2:
    numero1=numero-int(lista[0])*100
    listadesecuencia.append(numero1)
    #print(numero1)
    for m in str(numero1):
        lista.append(m)

    if len(str(numero1))==2:
        numero2=numero1-int(lista[1])*10
        listadesecuencia.append(numero2)
        #print(numero2)
#print(listadesecuencia)

#######################recoro el vector para encontrar los collats de listadesecuencia[n]

for x in listadesecuencia:
    x=n





