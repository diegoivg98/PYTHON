num_in:int = int(input('Ingrese numero inicial: '))
num_fin:int = int(input('Ingrese numero final: '))
numeros_impares = []

while num_fin <= num_in:
    num_fin:int = int(input('el segundo numero debe ser mayor que el primero. Usa otro numero: '))

for i in range(num_in,num_fin+1):
    if(i % 2 != 0):
        numeros_impares.append(i)

print(f"Lista de Números impares entre {num_in} y {num_fin}:")
print(numeros_impares)