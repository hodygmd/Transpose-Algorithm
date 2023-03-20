import numpy as np
print('Ingresar frase: ',end='')
frase=input()
pcount=0
paux=len(frase)/2+1
print('Caracteres totales (original):',len(frase))
print('Punto medio (+1):',paux)
for i in range(2,int(paux)):
    if len(frase)%i==0:
        pcount+=1
    if pcount!=0:
        print('El numero de caracteres NO es primo')
        print('No se realizan modificaciones a la cadena')
        break    
if pcount==0:
    print('El numero de caracteres SI es primo')
    if len(frase)%2!=0:
        frase=frase+' '
    print('Caracteres totales (new):',len(frase))
matrizS=[0,0]

count=0
for i in range(2,int(paux)):
    if i==int(paux)-1 and count!=0:
        break
    if len(frase)%i==0:
        matrizS[0]=i
        matrizS[1]=int(len(frase)/i)
        print(matrizS[0])
        print(matrizS[1])
        #if matrizS[0]<=10 and matrizS[1]<=10:
        #    break
        count+=1
    
print('La matriz sera de:',matrizS[0],'x',matrizS[1])
cifrado=np.zeros((matrizS[0],matrizS[1]),dtype=str)

c=1
for i in range(0,matrizS[0]):
    for j in range(0,matrizS[1]):
        cifrado[i][j]=frase[j*matrizS[0]+i:j*matrizS[0]+c+i]
        print(cifrado[i][j],end='')
    c+=1
print()
print()
print(cifrado)