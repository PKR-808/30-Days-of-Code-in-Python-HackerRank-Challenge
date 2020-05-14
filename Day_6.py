# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for i in range(0,t):
    s = input()
    j = len(s)
    u = ''
    v = ''
    for k in range(0,j):
        if k%2 == 0:
            u = u + s[k]
    print(u, end = ' ')
    for k in range(0,j):
        if k%2 != 0:
            v = v + s[k]
    print(v)
