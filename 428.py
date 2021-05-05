class University:
     def __init__(self):
         self.sl=None
         self.Dep=None
         self.Class=None
         self.student=None
         self.name=None
         self.id=None

class School:
    def __init__(self,name):
        self.name=name

class Department:
    def __init__(self,Dep):
        self.Dep=Dep




Shi=University()
Shi.sl=School("高科")
Shi.dep=Department("智慧商務")
