# Please modify the following program to now convert from input Fahrenheit
# to Celsius

def doConversion():
    tempInCAsString = input('Enter the temperature in Fahrenheit: ')
    tempInF = int( tempInCAsString )
    tempInC = (tempInF -32) / 1.8
    print('The temperature in Celsius is', tempInC, 'degrees')

for conversionCount in range( 3 ):
    doConversion()
    
