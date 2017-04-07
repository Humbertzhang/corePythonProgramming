#coding:utf-8

def getmon():
    global a,b
    a = input("Enter opening balance:")
    b = input("Enter monthly payment:")

def output(start,payment):
    bal = start
    paid = payment
    month = 0
    print "Pymt#   Paid    Balance"
    print "-----   -----   -------"
    print "0       0.00    $%5.2f"%(bal)
    month+=1
    while(bal > 0):
        print "%-4d   %-5.2f   $ %5.2f"%(month,paid,bal)
        month += 1
        bal -= paid
        if bal < paid:
            paid = bal

if __name__ == "__main__":
    getmon()
    output(a,b)

