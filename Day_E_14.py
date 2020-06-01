class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maxdiff = 0
        k=1
        for i in range(len(self.__elements)):
            for k in range(len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[k])
                if diff>maxdiff:
                     maxdiff = diff
        self.maximumDifference = maxdiff
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
