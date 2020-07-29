import msvcrt
def main():

#reciba un string como argumento en blanco y no supere los 50 caracteres
    r=calc("diegodiegodiegodiegodiegodiegodiegodiegodiegodiegodiego")
    x=calc("diego")
    s=calc("")
    print(r)
    print(s)
    print(x)

def calc(n):
    #SI EL STRING TIENE UN LARGO MENOR A 50 O NO CONTIENE
    if len(n)<50 or n==None:
        res="valido"
        return res

    else:
        res2="no valido"
        return res2
	


if __name__=="__main__":
    main()
    msvcrt.getch()
