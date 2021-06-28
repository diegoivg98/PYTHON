#CONVERTIR DECIMAL A BINARIO
nd = 5
lista = [] 
while nd != 0:
    lb = nd % 2
    cociente = nd // 2
    lista.append(lb) 
    nd = cociente 

print(lista)
