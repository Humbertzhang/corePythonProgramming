#coding:utf-8

import os

ls = os.linesep

fname = raw_input('>Filename: ')

print "Write Or Read Or Edit?"
model = raw_input('>input **"r"** for read or **"w"** for write new or **"e"** for edit one file already exists: ')

if model == "r":
    
    print "\n\n**Read Model**"
    
    if not os.path.exists(fname):
        print "\n*****Error: '%s' is NOT exists*****" %fname
    else:
        FileObj = open(fname,'r')
        print "File content:"
        for eachLine in FileObj:
            print eachLine.strip()
        FileObj.close()
    print '\n**Read Done**'
elif model == "w":
    print "Write Model"
    
    #查询是否重名
    if os.path.exists(fname):
        print "\n*****Error: '%s' already exists*****" %fname
        flag = 0
    else:
        flag = 1
    if flag:    
        #获取内容    
        content = []
        print "\nEnter lines ('.' to stop it)"
        while True:
            entry = raw_input('>Lines:')
            if entry == '.':
                break
            else:
                content.append(entry)
        #写内容
        fileObject = open(fname,'w')
        fileObject.writelines(['%s%s'% (x,ls) for x in content])
        fileObject.close()
        print '\n*Write Done*\n'
elif model == "e":
    print "**Edit Model**"
    if not os.path.exists(fname):
        print "\n*****Error: '%s' is NOT exists*****" %fname
    else:
        os.system('vim '+fname)  
    print "\n**Edit End**"
else:
    print "\n*****Error:No Such Model*****"
