#coding:utf-8

str = raw_input("Input a string:")
str = str.lower()
l = str.split(' ')
vowelnum = 0
connum = 0
vowel = ('a','e','i','o','u')
for i in range(len(str)):
    if str[i] in vowel:
        vowelnum+=1
    else:
        if str[i].isalpha():
            connum +=1
        else:
            continue

print "单词个数:",
print len(l)
print "元音字母个数：",
print vowelnum
print "辅音字母个数：",
print connum
