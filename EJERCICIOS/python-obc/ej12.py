def bisiesto():
  num: int = int(input('Introduce un número entero: '))
  if num % 4 == 0:
    print('es bisiesto')
    return True

  print('no es bisiesto')
  return False

print({bisiesto()})