fr = input("from num:")
to = input("to num:")
i = input("step num:")

while(True):
    print fr
    if (fr + i) <= to:
        fr += i
    else:
        break