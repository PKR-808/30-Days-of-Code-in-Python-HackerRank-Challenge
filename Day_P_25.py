# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

def checkPrime(num):
    for i in range(2, int(num**0.5+1)):
        if num%i == 0:
            return False
    return True
for i in range(T):
    n = int(input())
    if n>= 2 and checkPrime(n):
        print("Prime")
    else:
        print("Not prime")
