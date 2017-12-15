import random

import time

def diceWelcome():
    print("This program rolls two 6-sided dice until their sum is a given target value.")
    time.sleep(1.5) #force program to sleep for 1.5 seconds. 

def diceRoll( targetSum ):
    rollSum = 0
    countOfRolls = 0
    while True:
        randomRoll1 = random.randrange(1,7)
        randomRoll2 = random.randrange(1,7)
        countOfRolls += 1
        rollSum = randomRoll1 + randomRoll2
        print("Roll: {0} and {1}, sum is {2}".format(randomRoll1, randomRoll2, rollSum))
        if rollSum == targetSum:
            break
    print("Got it in {0} rolls!".format( countOfRolls ))
    
    
def main():
    diceWelcome()
    targetSum = int(input("Enter the target sum to roll for: "))
    print(' ')
    diceRoll( targetSum )
    
main()
