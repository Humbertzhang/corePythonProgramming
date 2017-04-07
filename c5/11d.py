#coding:utf-8

a,b = input(">请输入两个整数:"),input()

def check(a,b):
    if (a % b) == 0 or (b%a) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print check(a,b)
