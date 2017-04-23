num = input("The number of names:")
db = {}
for i in range(num):
    print "Please input name",
    print i,
    name = raw_input(":")
    namelist = name.split(' ')
    if not namelist[0].endswith(","):
        print "The format of input : Firstname, Lastname",
        print "Fixing..."
        namefir = namelist[0].split(',')
        namelas = namelist[1].split(',')
        db[namefir[0]] = namelas[0]
    else:
        db[namelist[0]] = namelist[1]

val = db.values()
key = db.keys()
db2 = dict(zip(val,key))
firlist = sorted(db2.keys())
print firlist
for a in range(num):
    print db2[firlist[a]],
    print firlist[a]
