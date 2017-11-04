bowlingSeries = 0

for i in [0,1,2]:
    GameScore = int(input("What was your bowling score?: "))
    bowlingSeries = GameScore + bowlingSeries
print("Your Series score is", bowlingSeries)
    