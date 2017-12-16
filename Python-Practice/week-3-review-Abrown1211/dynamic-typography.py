from graphics import *

userTypography = input("What message would you like to display?: ")

win = GraphWin('Dynamic Typography', 500, 500)
win.setBackground ('gray')

ordList = list(userTypography)

x = 0;
ordTemp = ''

"""The below for loop iterates over each character in the userTypography message
   and sets the Y value mutliplied by the ordinal value of the character to achieve the set point
   for ech character in the message.
   The text method is then used to set x and y points in the GraphWin to display the user inputted message."""

for chr in ordList:
    ordConversion = ord( chr )
    x = x + 25
    y = 5 + 1 * ordConversion
    message = Text(Point(x,y), chr)
    message.setTextColor('aqua')
    message.setFace('arial')
    message.setStyle('bold italic')
    message.setSize(20)
    message.draw(win)
    

win.getMouse()
win.close()


