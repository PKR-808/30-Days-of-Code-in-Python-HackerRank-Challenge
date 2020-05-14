#Shorter Code for Day 6 Problem

t = int(input())

for i in range(0, t):
    s = input()
    a = s[::2]
    b = s[1::2]
    print(a, b)
