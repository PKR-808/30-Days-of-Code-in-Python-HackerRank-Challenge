#!/bin/python3
#The additional codes of file write were already there in the HackerRank Python 3 Console
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)


    fptr.write(str(result) + '\n')

    fptr.close()
