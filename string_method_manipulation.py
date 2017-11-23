threeValueinput = eval(input("Enter your three numbers seperated by commas: "))

threeValueinput = list(threeValueinput)

valueAddition = 0

for index in range(len(threeValueinput)):
    valueAddition = valueAddition + threeValueinput[index]

print ("The sum is", valueAddition)
