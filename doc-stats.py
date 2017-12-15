def getTextFile():
    fileName = input("Enter the text file name: ")
    textFile = open( fileName, 'r' )
    return fileName, textFile

def outputCountResults( fileName, lineCount, wordCount, charCount,articleWordCount ):
    print()
    print( "******* {} *******".format( fileName ))
    print( "Line Count: {}".format( lineCount ))
    print( "Word Count: {}".format( wordCount ))
    print( "Char Count: {}".format( charCount ))
    print( "Total Non-Article Words: {}".format( articleWordCount ))
    
def countCharacters(line):
    charCount = 0
    for c in line:
        if not c.isspace():
            charCount = charCount + 1
    return charCount
    
def countWords( line ):
    words = line.split()        
    return len( words )

def countArticleWords( line ):
    wordList = ['a','an','the']
    words = 0
    for word in line.split():
        words += word.lower() not in wordList
    return words
    

def countDocStats( docFile ):
    lineCount = 0
    totalCharacters = 0
    totalWords = 0
    totalNonArticleWords = 0
    for line in docFile:
        lineCount += 1
        totalCharacters += countCharacters( line )
        totalWords += countWords( line )
        totalNonArticleWords +=countArticleWords( line )
    return lineCount, totalCharacters, totalWords, totalNonArticleWords

def main():
    fileName, textFile = getTextFile()
    lineCount, totalCharacters, totalWords,totalNonArticleWords = countDocStats( textFile )
    outputCountResults( fileName, lineCount, totalWords, totalCharacters , totalNonArticleWords)
    
main()