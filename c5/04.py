#coding:utf-8
year = input("输入一个年份:")
def judge(year):
    if ((year%4 == 0) and (year % 100 != 0)) or (year % 400 ==0):
        print "%d 是闰年" %year
    elif year <=0:
        print "错误输入"
    else:
        print "%d 不是闰年" %year
judge(year)
