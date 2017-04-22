import random
from random import randint

def geneSet():
    a = randint(0,10)
    lista=[]
    for i in range(a):
        lista.append(randint(0,10))
    seta = set(lista)
    return seta

if __name__ == "__main__":
    set1 = geneSet()
    print 'Set1',
    print set1
    set2 = geneSet()
    print  'Set2',
    print set2
    print 'A|B:',
    print (set1 | set2)
    print 'A&B:',
    print (set1 & set2)
