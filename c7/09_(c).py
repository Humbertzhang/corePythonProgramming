def tr(strori,straft,string):
    if not len(strori) >= len(straft):
        print "Wrong input."
        exit(0)
    strlist1 = list(strori)
    strlist2 = list(straft)

    l1 = len(strlist1)
    l2 = len(strlist2)

    while len(strlist2) < l1:
        strlist2 += [0]

    dictr = dict(zip(strlist1,strlist2))

    leg = len(string)
    str2 = ''

    for i in range(leg):
        if string[i] in strori:
            if dictr[string[i]] != 0:
                str2 += dictr[string[i]]
            else:
                pass
        else:
            str2 += string[i]

    return  str2

if __name__ == "__main__":
    s1 = raw_input("The Original str is: ")
    s2 = raw_input("After changed the str is: ")
    s3 = raw_input("The string you want to translate is: ")
    sp = tr(s1,s2,s3)
    print 'The string translated is:' + sp

