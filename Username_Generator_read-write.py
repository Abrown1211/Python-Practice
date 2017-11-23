inputFileName = input("Enter the filename with user's names: ")
outputFileName = input("Enter the filename to write the user names to: ")

inFile = open( inputFileName, "r" )
outFile = open( outputFileName, "w" )

namesSeq = inFile.readlines()

for name in namesSeq:
    splitName = name.strip().split(" ")
    firstName = splitName[0]
    lastName = splitName[1]
    
    userName = firstName[0] + lastName[:7]
    userName = userName.lower()
    print( userName, file=outFile )
    
inFile.close()
outFile.close()

print ("Your file has been processed successfully!")

    
    
    