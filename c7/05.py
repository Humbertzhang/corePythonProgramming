#!/usr/bin/env python

''' 
the (b),(e),(f) for 7-5 exercise
'''

db = {}

def newuser():
    flag =1
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        forbidden =' !@#$%^&*()_-+=,<.>/?\|'
        forbidden = list(forbidden)
        for i in range(len(forbidden)):
            if forbidden[i] in name:
                print "'",forbidden[i],"'"
                print 'is illeagle charactor'
                flag = 0
                break
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    if flag ==1:
        pwd = raw_input('passwd: ')
        name = name.lower()
        db[name] = pwd

def olduser():
    name = raw_input('login: ')
    name = name.lower()
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        pass
    else:
        print 'login incorrect'
        return

    print 'welcome back', name

def govern():
    token = 0
    psw = '11223344'
    pwd = raw_input("govern passwd:")
    if pwd == psw:
        token = 1
        print "It's Your World, My Load. "
    else:
        print "Wrong! You are a liar!"
        exit(2333)
    while True:
        choiceg = raw_input("d for del a user,l for list all the users, e for exit:")
        if choiceg == 'd':
            usrname = raw_input("Please input the user's name:")
            usrname = usrname.lower()
            print "Removed",
            print usrname
            db.pop(usrname)

        elif choiceg == 'l':
            for i in range(len(db)):
                print 'Username:',
                print (db.keys())[i],
                print 'Password:',
                print (db.values())[i]
        elif choiceg == 'e':
            break;



def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
(G)overn
Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            if choice not in 'neqg':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'g': govern()

if __name__ == '__main__':
    showmenu()