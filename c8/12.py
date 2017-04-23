#coding:utf-8
start = input("Start:")
end = input("End:")
list1=[]
for i in range(start,end+1):
    list1.append(i)

if end >= 33:
    asciiable = True
else:
    asciiable = False

if asciiable:
    print "十进制        二进制        八进制        十六进制        ASCII"
    print "--------" * 7
    for i in range(start,end+1):
        print '%d          ' %i,
        print bin(i),
        print '           ',
        print '%o          ' %i,
        if i >= 33:
            print '%x          ' %i,
            print chr(i)
        else:
            print '%x          ' % i
else:
    print "十进制        二进制        八进制        十六进制"
    print "--------" * 6
    for i in range(start,end+1):
        print '%d          ' %i,
        print bin(i),
        print '           ',
        print '%o          ' %i,
        print '%x          ' %i

