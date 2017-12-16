#area computer menu. Creates menu selection and feedback only, does not calculate area. 

def userGUI():
    print("Welcome to the area computation tool!\n")
    print("****** MENU ******\n")
    print("tri    Compute area of a triangle\ntrap   Compute area of a trapezoid\ncir    Compute area of a circle")
    print("quit   Quit the tool")
    
def userInput():
    while True:
        userChoice = input("Please enter your choice:  ")
        if userChoice not in ('tri', 'cir', 'trap','quit'):
            print("Invalid choice: {0}".format( userChoice ))
        else:
            print("You chose: {0}".format( userChoice ))
            break
        

def main():
    userGUI()
    userInput()
    
main()
    