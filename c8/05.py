#coding:utf-8

def getfactors(num):
    factors = []
    i = 1
    while i < num:
        if num % i == 0:
            factors.append(i)
        i+=1
    return factors

if __name__ == "__main__":
    n = input("Input a number:")
    fac = getfactors(n)
    print '约数：',
    print fac