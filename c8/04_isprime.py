def isprime(num):
    a = num/2
    while(a > 1):
        if num%a == 0:
            a-=1
            continue
        else:
            flag = True
            break
    else:
        flag = False

    return flag

if __name__ == "__main__":
    n = input("Please input a number:")
    print isprime(n)

