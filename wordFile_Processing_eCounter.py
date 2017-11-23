#processing a file with an indefinite While loop.

fileNames = ["words_1.csv", "words_2.csv", "words_3.csv"]

totalNumberOfEs = 0

for fileName in fileNames:
    wordsFile = open( fileName, 'r')
    
    nextLine = wordsFile.readline()
    while nextLine != '':
        words = nextLine.split(',')
        for word in words:
            numberOfEs = word.count('e')
            totalNumberOfEs = totalNumberOfEs + numberOfEs
            nextLine = wordsFile.readline()
    wordsFile.close()

print("The total number of e's is {0}.".format( totalNumberOfEs))

    