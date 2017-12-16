# Please do your work for problem one in this file

import math

QtyOfBowlingBalls = eval(input("How many bowling balls will be manufactured? "))
diaOfBowlingBall = eval(input("What is the diameter of each ball in inches? "))
coreVolume = eval(input("What is the core volume in inches cubed? "))

def SphereVol(diaOfBowlingBall):
    radius = diaOfBowlingBall/2
    volume = 4/3*math.pi* radius**3
    return volume

BowlingBallVol = SphereVol(diaOfBowlingBall)
FillerVolume = (BowlingBallVol - coreVolume) * QtyOfBowlingBalls

print("You will need " + str(FillerVolume) + " inches cubed of filler")