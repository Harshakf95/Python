class grandfather:
    def __init__(self,gn):
        self.gname=gn
    def display1(self):
        print("I am grandfather,My Name is:",self.gname)
class father(grandfather):
    def __init__(self, fn, gn):
        self.fname=fn
        super().__init__(gn)
    def display2(self):
        print("I am father,My Name is:",self.fname)
class child(father):
    def __init__(self, cn1, cn2, fn, gn):
        self.cname1=cn1
        self.cname2=cn2
        super().__init__(fn, gn)
    def display3(self):
        print("I am child1,My Name is:",self.cname1)
        print("I am child2,My Name is:",self.cname2) 
# class child2(father):
#     def __init__(self, cn, fn, gn):
#         self.cname=cn
#         super().__init__(fn, gn)
#     def display3(self):
#         print("I am child,My Name is:",self.cname)
c=child("Lava","Kusha","Rama","Dasharatha")
# c2=child2("Kusha","Rama","Dasharatha")
c.display1()
c.display2()
c.display3()
# c2.display1()
# c2.display2()
# c2.display3()