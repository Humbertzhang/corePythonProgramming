string = raw_input("Please input a string:")
le = len(string)
str1 = list(string)
str=''
for i in range(le):
    if not str1[i].isalpha():
        str+=str1[i]
        continue
    if str1[i].islower() and str1[i]:
        cha = str1[i].upper()
    if  str1[i].isupper():
        cha = str1[i].lower()
    str+=cha
print str