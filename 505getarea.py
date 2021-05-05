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


class Sidelength:
    def __init__(self,l=0):
        self.l=l
    
    def get_area(self):
        return self.l*self.l

    def get_metar(self):
        return self.l*4


R1 =Sidelength(6)
print("長",R1.l," ","面積為",R1.get_area()," ","邊長為",R1.get_metar())


