from math import pi


class Circle:
    def __init__(self,r=1.0):
        self.r=r

    def get_area(self):
        return pi*self.r*self.r

C1 =Circle(10)
print(C1.get_area())
C2 =Circle(20)
print(C2.get_area())

