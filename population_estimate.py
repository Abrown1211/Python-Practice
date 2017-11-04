import math


initialPopulation = int(input("What is the population you wish to calculate: "))
grow_decayRate =  float(input("What is the Growth or Decay rate: "))
NumberofYears =   int(input("How many years do you wish to estimate: "))

population = initialPopulation * (math.exp(grow_decayRate * NumberofYears))

print (population)
