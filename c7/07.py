def excKeyValue(dic):
    orikey = dic.keys()
    orivalue = dic.values()
    dicret = dict(zip(orivalue,orikey))
    return dicret

if __name__ =="__main__":
    dic = {'key1':'value1','key2':'value2'}
    dic2 = excKeyValue(dic)
    print dic2