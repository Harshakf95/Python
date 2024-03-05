w=eval(input("enter weight(in kgs)"))
h=eval(input("enter height(in inches)"))
m=0.025*h
bmi=w/(m*m)
print("Body Mass Index for given inputs:",bmi)
if bmi>0 and bmi<18:
    print("BMI stage :Low Weight")
elif bmi>=18 and bmi<25:
    print("BMI stage : Perfect")
else:
    print("BMI stage : Overweight")        