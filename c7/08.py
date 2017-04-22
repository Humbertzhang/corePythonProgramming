db = {}
while True:
    name = raw_input("Input a name(0 to exit):")
    if name == '0':
        break
    id = raw_input("Input the id:")
    db[name] = id

l = len(db)
names = sorted(db.keys())
for i in range(l):
    print 'Name:',
    print names[i],
    print 'Id:',
    print db[names[i]]


