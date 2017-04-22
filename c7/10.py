def rot13(str):
    str1 = "abcdefghijklmnopqrstuvwxyz"
    list1 = list(str1)
    str2 = "nopqrstuvwxyzabcdefghijklm"
    list2 = list(str2)
    dic = dict(zip(list1,list2))
    strret=''
    length = len(str)

    for i in range(length):
        if str[i] in str1:
            strret += dic[str[i]]
        else:
            strret += str[i]

    return strret

if __name__ == '__main__':
    string = raw_input("Enter a string that you want to rot13 it:")
    string = string.lower()
    straft = rot13(string)
    print "The string rot13ed is:"
    print straft