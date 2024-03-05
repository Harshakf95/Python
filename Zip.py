name = []
score = []
n = int(input("Enter how many players: "))
for i in range(0,n):
    name.append(input("Enter the player name: "))
    score.append(input("Enter the score: "))
z = zip(name,score)
d = dict(z)
print(d)
name = input("Enter name of player for sore: ")
print("The score is: ",d[name])