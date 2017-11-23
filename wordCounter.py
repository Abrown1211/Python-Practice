numberOfWords = 0
countOfEs = 0
totalLengthOfInputs = 0

sentinel = 'quit'

inputWord = input("Enter word {0}: ".format( numberOfWords))

while inputWord != sentinel:
    numberOfWords = numberOfWords + 1
    countOfEs = countOfEs + inputWord.count('e')
    totalLengthOfInputs = totalLengthOfInputs + len(inputWord)
    
    inputWord = input("Enter word {0}: ".format( numberOfWords))
    
print("Total e's seen: ", countOfEs)
print("Percent of e's: {:0.2}%".format( countOfEs / totalLengthOfInputs))
print("Average of e's seen: {:0.2}".format( countOfEs / numberOfWords))
    
