def decor(fun):
    def check():
        x=fun()
        if(x.isdigit()!=True):
            print("Invalid Phone Number,re enter phone number")
            return check()
        if(len(x)!=10):
            print("Phone number should be 10 digits, re enter phone number")
            return check()
        return x
    return check
@decor
def accept():
    n=input("Enter your phone number:")
    return n
print("Entered Phone number is:",accept())