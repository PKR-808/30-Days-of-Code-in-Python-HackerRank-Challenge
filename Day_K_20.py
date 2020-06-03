#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_count = 0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            swap_count += 1
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    if swap_count == 0:
        break
print('Array is sorted in '+str(swap_count)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[n-1]))
