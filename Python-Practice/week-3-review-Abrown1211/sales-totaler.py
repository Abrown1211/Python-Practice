inputFileName = input("Enter sales file name: ")
outputFileName = input("Enter name for total sales file: ")

inputFile = open( inputFileName, 'r' )
outputFile = open( outputFileName, 'w' )

readSales = inputFile.readlines()

for numbers in readSales:
    splitDollar = numbers.strip('\n').replace('$', '').split(' ')
    firstSale = float(splitDollar[0])
    secondSale = float(splitDollar[1])

    total = firstSale + secondSale

    message = '$ {:7.2f}  $ {:7.2f}  $ {:7.2f}\n'.format(firstSale, secondSale, total)
    outputFile.write(message)

inputFile.close()
outputFile.close()
        
print("\nDone writing totals to: {0}".format(outputFileName))   

