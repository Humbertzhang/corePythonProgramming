#coding:utf-8
import random

elenum = random.randint(1,100)
sequ=[]
for i in range(elenum):
    sequ.append(random.randint(0,2**31 - 1))

elenum2 = random.randint(1,elenum)
sequ2=[]
for i in range(elenum2):
    parts = random.choice(sequ)
    sequ.remove(parts)
    sequ2.append(parts)

sequ2.sort()
print sequ2
