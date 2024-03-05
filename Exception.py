class MyException(Exception):
    def __init__(self, args):
        self.msg=args
def check(dict):
        for k,v in dict.items():
            print("Name=",k,"Balance=",v)
            if v<2000.00:
                raise MyException("Balance amount is less in the account of"+k)
n=int(input("Enter number of Customers:"))
bank={input("Enter Name:"):int(input("Enter Balance:"))for i in range(n)}
try:
    check(bank)
except MyException as me:
    print(me)