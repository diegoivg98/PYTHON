def numprimo():
  num: int = int(input('Introduce un número entero: '))
  for i in range(2,num):
    if num % i == 0:
        print('no es primo')
        return False
  
  print('es primo')
  return True



print({numprimo()})