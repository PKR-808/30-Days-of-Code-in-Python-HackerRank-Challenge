# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculateFine(a,o):
    fine = 0
    if a[2]>o[2]:
        fine = 10000
    elif a[2]==o[2]:
        if a[1]>o[1]:
            fine = (a[1] - o[1])*500
        elif a[1]==o[1]:
            if a[0]>o[0]:
                fine = (a[0] - o[0])*15
    return fine


a = [int(e) for e in input().split(' ')]
o = [int(i) for i in input().split(' ')]

print(calculateFine(a,o))
