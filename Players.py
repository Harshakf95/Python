name=[]
score=[]
n=int(input("Enter how many players?"))
for i in range(0,n):
    name.append(input("Enter Player name:"))
    score.append(input("Enter score:"))
z=zip(name,score)
d=dict(z)
print(d)
name=input("Enter name of player for score:")
print("The Score is:",d[name])