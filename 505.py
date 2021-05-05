class Car:
    def __init__(self):
        self.en=None
        self.fr=None
        self.fl=None
        self.br=None
        self.bl=None
class Wheel:
    def __init__(self,size):
        self.size=size

class Engine:
    def __init__(self,cc):
        self.cc=cc

a=Car()
a.en=Engine(2500)
a.fr=Wheel(40)
a.fl=Wheel(40)
a.br=Wheel(40)
a.bl=Wheel(40)

class Car1:
    def __init__(self):
        self.en=None
        self.wls=None
b=Car1()
b.en=Engine(2500)
b.wls=[]
for i in range(8):
    tmp=Wheel(50)
    b.wls.append(tmp)

