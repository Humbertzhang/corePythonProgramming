#coding:utf-8

def getMoney():
    global money
    money = input("请输入一个小于1美元的钱数:")

def giveMoney(mon):
    flag,cent25,cent10,cent5,cent1 = 0,0,0,0,0
    if mon > 1 :
        flag = 1
        print "Wrong Input"
    while(mon > 0.0001 and flag == 0):
        if mon >= 0.25:
            cent25 += 1
            mon -= 0.25
        elif mon >= 0.10:
            cent10 += 1
            mon -= 0.10
        elif mon >= 0.05:
            cent5 += 1
            mon -= 0.05
        elif mon >= 0.01:
            cent1 += 1
            mon -= 0.01
        #print mon
        #raw_input()
    if (flag == 0):
        print "可以换成%d 个25美分 %d 个10美分 %d 个5美分 %d 个1美分" %(cent25,cent10,cent5,cent1)

if __name__ == "__main__":
    getMoney()
    giveMoney(money)
