#coding:utf-8
from __future__ import division

def getF():
    global f
    f = input(">请输入一个华氏温度:")

def conver(f):
    c = (f-32)*(5/9)
    print "\n>摄氏温度:%.2f" %c

if __name__ == "__main__":
    getF()
    conver(f)
    
