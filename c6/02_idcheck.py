import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print "Welcome to the Black Parade"
myInput = raw_input("Identifier to test?:")

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''Invalid: first symbol must be alphabetic'''
    elif myInput in keyword.kwlist:
        print '''Invalid: input is keyword.'''
    else:
        for otherChar in myInput[1:]:
            if (otherChar not in alphas + nums):
                print '''Invalid: remaining symbols must be alphanumeric'''
                break
            print "it's an indentifier."
elif len(myInput) ==1:
    if myInput not in alphas + nums:
        print '''Invalid: first symbol must be alphabetic'''
    else:
        print '''It's an indentifier.'''




