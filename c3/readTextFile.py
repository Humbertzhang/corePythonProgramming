#coding:utf-8
import os
#get filename
fname = raw_input('Enter filename:')
print 

#attempt to open file for reading
if os.path.exists(fname):
    fobj = open(fname,'r')
    for eachLine in fobj:
        print eachLine.strip()
    fobj.close()
else:
    print "***file open error:No Such File."
