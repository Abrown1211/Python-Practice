welcomeMessage = print("Welcome to the Golf Club Helper!\nTell me your situation, and I'll recommend a club")

ontheGreen = input("\nDid you hit it on the green (y/n)?: ")
distanceFromPin = int(input("How far is the ball from the hole?: "))

golfClubType = ''

if ontheGreen is 'y':
    clubType = "Putter"
    
elif distanceFromPin >= 200:
    clubType = "Driver"
    
elif distanceFromPin > 140 < 199:
    clubType = "5-Iron"
    
elif distanceFromPin > 100 < 140:
    clubType = "9-Iron"
    
elif distanceFromPin > 15 < 99:
    clubType = "Pitching Wedge"
    
elif distanceFromPin <=15:
    clubType = "Putter"
    
                    
print ("\nI recommend using your" , clubType)
