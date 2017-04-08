def strip(sen):
    sen = list(sen)
    length = len(sen)
    i = 0
    #print sen

    while(i < length):
        #print i
        #print sen
        try:
            sen.remove(' ')
        except ValueError:
            break
        i += 1

if __name__ == "__main__":
    sentence = raw_input(">Please input a word maybe with ' ':")
    out = strip(sentence)
    print out

