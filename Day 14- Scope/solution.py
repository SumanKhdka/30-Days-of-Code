class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
   
        self.maximumDifference = 0

    def computeDifference(self):
        
        for i in self.__elements:
            for j in self.__elements:

                diff = abs(i - j)
                
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
        



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)