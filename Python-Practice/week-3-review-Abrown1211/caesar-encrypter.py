inputFileName = input("Enter the filename to be used for encryption: ")
key = int( input("Enter the shift key: " ))
outputFileName = input("Enter the output file name: " )

inFile = open( inputFileName, "r" )
outFile = open( outputFileName, "w" )

CaesarEncrypt = inFile.readlines()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

#print( alphabet )
#print( shiftedAlphabet )

encryptedMessage = ''

for line in CaesarEncrypt:
    for character in line():
        letterIndex = alphabet.find( character )
        encryptedCharacter = shiftedAlphabet[letterIndex]
        #print( "{0} -> {1}".format( character, encryptedCharacter ) )
        encryptedMessage = encryptedMessage + encryptedCharacter
    
print ("The encrypted message is: {0}".format( encryptedMessage ))

outputFile = open( outputFileName, "w" )
print( encryptedMessage, file=outputFile )
inFile.close()
outputFile.close()

print( "Done writing encrypted message to file {0}".format( outputFileName))
