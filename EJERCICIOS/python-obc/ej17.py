import os

file = open("archivo.txt", "w")
file.write("escribiendo documento" + os.linesep)
file.close()

file = open('archivo.txt', 'r+')
file.readline()

file.seek(0)
print(file.read())
file.close()