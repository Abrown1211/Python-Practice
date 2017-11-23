lowerOrd = int(input("Enter the lower ordinal bound: "))
upperOrd = int(input("Enter the upper ordinal bound: "))

ordList = list(range(lowerOrd, upperOrd))

#def decrypt(ordList):
ordTemp = ''
for ord in ordList:
    ordConversion = chr( ord )
    ordTemp = ordTemp + " " + ordConversion
        #ordTemp.append((chr( ord)))
    #return ordTemp

print ("The characters from" , lowerOrd, "to" , upperOrd, "are:",end=ordTemp)
