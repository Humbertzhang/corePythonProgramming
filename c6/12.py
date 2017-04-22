def findchr(string,char):
    l = len(string)
    for i in range(l):
        if string[i] == char:
            return i
    return -1

def rfindchr(string,char):
    l = len(string)
    i = l-1
    while(i>0):
        if string[i] == char:
            return i
            break
        else:
            i+=1
    return -1

def subchr(string,orichar,newchar):
    l = len(string)
    flag = -1
    for i in range(l):
        if string[i] == orichar:
            flag = i
            break
    if flag != -1:
        str2 = string[:flag]+newchar+string[flag+1:]
        return str2
    else:
        str2 = "No such character."
        return  str2

if __name__ == "__main__":
    str = raw_input("Please input a string:")
    char = raw_input("Please input a character:")
    type = input("0 for from head to tail,1 for from tail to head,2 for instead it:")
    if len(char)>1:
        print "Illegal input for character"
    else:
        if type == 0:
            index = rfindchr(str,char)
        elif type == 1:
            index = findchr(str,char)
        elif type == 2:
            newchar = raw_input("Please input a char that u want to instead the old one.")
            strret = subchr(str,char,newchar)
            print strret