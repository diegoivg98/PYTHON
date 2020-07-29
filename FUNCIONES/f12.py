import msvcrt
def main():

#reciba un string como argumento
    r=calc("diego","diego")#CUMPLE
    a=calc("die","go")#NO CUMPLE
    print(r)
    print(a)

def calc(n,m):
    #SI SE IGUALAN
    if n==m:
        return 1
    else:
        return 0
    


if __name__=="__main__":
    main()
    msvcrt.getch()
