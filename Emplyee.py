class Employee:
    def __init__(self,id,name,sal):
        self.eid=id
        self.ename=name
        self.esal=sal
    def display(self):
        print("Emp-id:",self.eid)
        print("Emp-name:",self.ename)
        print("Emp-sal:",self.esal)
e=[]
n=int(input("Enter number of employees:"))
for i in range(1,n+1):
    print("Enter emp-id,name and salary of Employee-",i)
    e.append(Employee(int(input()),input(),float(input())))
i=1
for obj in e:
    print("Employee-",i,"information")
    obj.display()
    i=i+1