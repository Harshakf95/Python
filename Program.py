# import math
# n=eval(input("Enter the number:"))
# print("Float absolute value of",n,"is:",math.fabs(n))
# print("Ceil value of",n,"is:",math.ceil(n))
# print("Floor value of",n,"is:",math.floor(n))
# print("Exponential value of",n,"is:",math.exp(n))
# print("Log value of",n,"is:",math.log(n))
# print("Natural logarithm value of",n,"is:",math.log10(n))
# print("Sine value of",n,"is:",math.sin(n))
# print("Cosine value of",n,"is:",math.cos(n))
# print("Tangent value of",n,"is:",math.tan(n))
# print("Degree value of",n,"is:",math.degrees(n))
# print("Radians value of",n,"is:",math.radians(n))
# print("Square root value of",n,"is:",math.sqrt(n))
#################################
# w = eval(input("Enter weight(in kgs)"))
# h = eval(input("Enter height(in inches)"))
# m = 0.025*h
# bmi = w/(m*m)
# print("Body mass index for given inputs:",bmi)
# if bmi>0 and bmi<18:
#     print("BMI stage:Low Weight")
# elif bmi>=18 and bmi<25:
#     print("BMI stage:Perfect")
# else:
#     print("BMI stage:Over Weight")
################################
# maxmarks = int(input("Enter maximum marks:"))
# maxobt = int(input("Enter total marks obtained:"))
# per = maxobt*(100/maxmarks)
# if per>=90.01 and per<=100:
#     Grade = "O Outstanding"
# elif per>=80.01 and per<=90:
#     Grade = "A++ First Class"
# elif per>=70.01 and per<=80:
#     Grade = "A+ First Class"
# elif per>=60.01 and per<=70:
#     Grade = "A First Class"
# elif per>=55.01 and per<=60:
#     Grade = "B+ Higher Second Class"
# elif per>=50.01 and per<=55:
#     Grade = "B Second Class"
# elif per>=40.01 and per<=50:
#     Grade = "Pass Class"
# elif per>=0 and per<=40:
#     Grade = "Fail"
# else:
#     print("Invalid Percentage")
# print("Percentage:",round(per,2))
# print("Grade:",Grade)
################################
# a =[1,3,5,6,7,7,[1,3,5],'hello']
# print(a)
# a.insert(3,20)
# print(a)
# a.remove(7)
# print(a)
# a.append('hi')
# print(a)
# print(len(a))
# a.pop()
# print(a)
# a.clear()
# print(a)
################################
# name = []
# score = []
# n = int(input("Enter how many players:"))
# for i in range(0,n):
#     name.append(input("Enter the player name:"))
#     score.append(input("Enter score:"))
# z = zip(name,score)
# d = dict(z)
# print(d)
# name = input("Enter name of player for score:")
# print("The score is:",d[name])
################################ 
# class Employee:
#     def __init__(self,id,name,sal):
#         self.eid=id
#         self.ename=name
#         self.esal=sal
#     def display(self):
#             print("Emp-id:",self.eid)
#             print("Emp-name:",self.ename)
#             print("Emp-sal:",self.esal)
# e=[]
# n=int(input("Enter number of employees:"))
# for i in range(1,n+1):
#     print("Enter emp-id,emp-name, and salary of employee-",i)
#     e.append(Employee(int(input()),input(),float(input())))
# i=1
# for obj in e:
#     print("Employee-",i,"information")
#     obj.display()
#     i=i+1
##################################
class grandfather:
    def __init__(self,gn):
        self.gname=gn
    def display1(self):
        print("I am grandfather, My name is:",self.gname)
class father(grandfather):
    def __init__(self, fn, gn):
        self.fname=fn
        super().__init__(gn)
    def display2(self):
        print("I am father, My name is:",self.fname)
class child(father):
    def __init__(self, cn, fn, gn):
        self.cname=cn
        super().__init__(fn, gn)
    def display3(self):
        print("I am child, My name is:",self.cname)
c=child("Lava-Kusha","Rama","Dasharatha")
c.display1()
c.display2()
c.display3() 