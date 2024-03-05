# m1=eval(input("Enter the marks of Python: "))
# m2=eval(input("Enter the marks of Computer Networks: "))
# m3=eval(input("Enter the marks of OS: "))
# m4=eval(input("Enter the marks of Hindi/Sanskrit: "))
# m5=eval(input("Enter the marks of English: "))
# total=(m1+m2+m3+m4+m5)
# print(total)
# per=(total/500)*100.0
# print(per)
# if per>75:
#     print("Grade A")
# elif per>60 and per<75:
#     print("Grade B")
# elif per>50 and per<60:
#     print("Grade C")
# else:
#     print("Grade D")

maxmarks = int(input("Enter maximum marks: "))
marksobt = int(input('Enter total marks obtained: '))
per = marksobt*(100/maxmarks)
if(per>=90.01 and per<=100):
    grade = "O Outstanding"
elif(per>=80.01 and per<=90):
    grade = "A++ First Class"
elif(per>=70.01 and per<=80):
    grade = "A+ First Class"
elif(per>=60.01 and per<=70):
    grade = "A First Class"
elif(per>=55.01 and per<=60):
    grade = "B+ Higher Second Class"
elif(per>=50.01 and per<=55):
    grade = "B Second Class"
elif(per>=40.01 and per<=50):
    grade = "Pass Class"
elif(per>=0 and per<=40):
    grade = "Fail"
else:
    print("Invalid Percentage")
print("Percentage:",round(per,2))
print("Grade:",grade)
