from graphics import *

userTypography = input("What message would you like to display?: ")
win = GraphWin('Dynamic Typography', 500, 1000)

ordList = list(userTypography)

x = 0;
y0 = 150
ordTemp = ''
for chr in ordList:
    ordConversion = ord( chr )
    x = x + 50
    y = y0  - ordConversion
    if x > 500:
        x = 50
        y0 += 100
        y += 100
        
    print(chr, ordConversion, x, y)
    message = Text(Point(x,y), chr)
    message.setTextColor("blue")
    message.setSize(20)
    message.draw(win)
    

win.getMouse()
win.close()