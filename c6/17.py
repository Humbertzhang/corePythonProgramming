def mypop(lista):
    a = lista[-1]
    return a

if __name__ == '__main__':

    lista = raw_input("Input a string and i will change it to a list:")
    lista = list(lista)
    print "Origin:",
    print lista

    popeda =  mypop(lista)
    print "Poped:",
    print popeda

    print "Now:",
    lista = lista[:-1]
    print lista