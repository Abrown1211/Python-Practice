#password checker, checks the length of a password input for validation.

while True:
    newPassword = input("Enter your new password: ")
    while True:
        if len(newPassword) > 7:
            break
        print("Your password must be at least seven characters long")
        newPassword = input("Enter your new password: ")
    retypePassword = input("Enter your password again: ")
    if newPassword == retypePassword:
        break
    print("Your passwords do not match.")
    
    
print("Your new password is {0}.".format( newPassword))
