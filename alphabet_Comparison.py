#method using 3 inputs from a user to compare 3 values
"""firstwordInput = input("Enter a word to compare: ")
secondwordInput = input("Enter a another word to compare: ")
thirdwordInput = input("Enter a one last word to compare: ")"""

#wordCompare = wordInput.split(",")
#program number 1, all if statements
"""if firstwordInput < secondwordInput:
    print("{0} comes first in the alphabet".format(firstwordInput))
elif secondwordInput < thirdwordInput:
    print("{0} comes first in the alphabet".format(secondwordInput))
elif firstwordInput < thirdwordInput:
    print("{0} comes first in the alphabet".format(firstwordInput))
else:
    print("{0} comes first in the alphabet".format(thirdwordInput))"""

#same program using nested if statements
"""if firstwordInput < secondwordInput:
    if firstwordInput < thirdwordInput:
        print("{0} comes first in the alphabet".format(firstwordInput))
    else:
        print("{0} comes first in the alphabet".format(thirdwordInput))
else:
    print("{0} comes first in the alphabet".format(secondwordInput))"""

#final program using a for loop to iterate through word comparisons to find the first word in the alphabet.     
numofIterations = int(input("Enter the number of words you would like to compare: "))

firstAlpha = input("Enter a word to compare: ")

for index in range(numofIterations - 1):
    nextWord = input("Enter the next word to compare: ")
    if nextWord < firstAlpha:
        firstAlpha = nextWord
else:
    print("The words are the same place in the alphabet")
        
print("{0} comes first in the alphabet".format(firstAlpha))
    