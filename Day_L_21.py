#Python wasn't enabled in the HackerRank editor 
#I have used the Test Case 1 of the Day21 challenge as the input for Python version of this problem.

from typing import TypeVar

Vector = TypeVar("Vector")


def printArray(vect: [Vector]):
    for v in vect:
        print(v)


int_vector = [8, 6, 7, 5, 3, 0, 9]
string_vector = ["Jenny's", "Phone", "Number"]

printArray(int_vector)
printArray(string_vector)
