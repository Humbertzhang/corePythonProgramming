#coding:utf-8
def scan(str1,str2):
    l1=len(str1)
    l2=len(str2)
    flag = 0
    if l1 != l2:
        print "不匹配"
    else:
        for i in range(l1):
            if str1[i] != str2[i]:
                print "不匹配"
                flag = 1
                break
        if flag==0:
            print "匹配"

if __name__ =="__main__":
    string1=raw_input("Str1:")
    string2=raw_input("Str2:")
    scan(string1,string2)

