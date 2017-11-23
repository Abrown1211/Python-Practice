kmValue = float(input("Enter the distance in km: "))

if kmValue >= 0:
    milesValue = kmValue / 1.609
    print("{0:0.2f} km is the same as {1:0.2f} mi".format( kmValue, milesValue))
    print(" Thanks for converting!")
else:
    print("Negative value conversions are not allowed. Try a positive integer value")
        


