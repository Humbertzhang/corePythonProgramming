#coding:utf-8
a = raw_input(">Please input a string:")
b = list(a)
rmed = 0
#b为偶数
if len(b)%2 == 0:
    i = len(b)/2 -1
    while(i>=0):
        print b[i]
        print b[i+1+rmed*2]
        i -=1
        rmed +=1


elif len(b)%2 ==1:
    i = len(b)/2-1
    print b[i+1]
    while(i>=0):
        print b[i]
        print b[i+2+rmed*2]
        i -= 1
        rmed += 1
