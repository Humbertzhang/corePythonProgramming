import time
user = raw_input("Input your chioce like stone,scissor or cloth:")

if user != "stone" or "scissor" or "cloth":
    print "Illegal Input"
    exit(0)

a = time.time()
a = a - int (a)

if a >=0 and a<=0.333:
    ret = "stone"
elif a >= 0.333 and a <= 0.667:
    ret = "scissor"
else:
    ret = "cloth"

print 'My choice is.....'
print ret + '!'
print 'So',
if user == ret:
    print "We Tie!"
elif (user =="stone" and ret == "cloth") or (user =="cloth" and ret =="scissor") or (user == "scissor" and ret =="stone"):
    print "You Lose!"
else:
    print "You Win!"





