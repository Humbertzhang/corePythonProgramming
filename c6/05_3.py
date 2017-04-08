#coding:utf-8
str = raw_input("string:")

def check(str):
    length = len(str)
    mid = length / 2
    if len(str) % 2 == 0:
        if str[:mid] == str[mid:length]:
            print "重现"
        else:
            print "不重现"
    elif len(str) % 2 == 1:
        if str[:mid] == str[mid+1:length]:
            print "重现"
        else:
            print "不重现"
    if len(str) % 2 == 0:
        strf = str[:mid]
        strb = str[mid:length]
        strfl = list(strf)
        strbl = list(strb)
        strbl.reverse()
        if strfl == strbl:
            print "回文"
        else:
            print "不回文"
    elif len(str) % 2 == 1:
        strf = str[:mid]
        strb = str[mid+1:length]
        strfl = list(strf)
        strbl = list(strb)
        strbl.reverse()
        if strfl == strbl:
            print "回文"
        else:
            print "不回文"

if len(str) == 1:
    print "重现"
    print "回文"
else:
    check(str)