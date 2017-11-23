firstWord = input("Enter the first word you would like to compare: ")
secondWord = input("Enter the second word you would like to compare: ")

x1 = firstWord
x2 = secondWord

if len(x1) > len(x2):
    print("The length of the {0} is greater than the length of {1}.".format( x1, x2))
elif len(x2) > len(x1):
    print("The length of the {1} is greater than the length of {0}.".format( x1, x2))
else:
    print("Its a tie!")
    
