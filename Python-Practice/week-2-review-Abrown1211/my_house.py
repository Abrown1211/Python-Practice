# Please do your work for problem three in this file

import graphics as g
win = g.GraphWin('My House', 400,400)

blueSky = g.Rectangle(g.Point(0,0), g.Point(400,300))
blueSky.setFill('Light Sky Blue')
blueSky.draw(win)

bottomHouse = g.Rectangle (g.Point(100,125), g.Point (300, 300))
bottomHouse.setFill ('Indian Red')
bottomHouse.draw(win)

firstWindow = g.Rectangle (g.Point(130,220), g.Point (150, 250))
firstWindow.setFill ('Light Gray')
firstWindow.draw(win)

secondWindow = g.Rectangle (g.Point(250,220), g.Point (270, 250))
secondWindow.setFill ('Light Gray')
secondWindow.draw(win)

frontDoor = g.Rectangle (g.Point(180,220), g.Point (220, 300))
frontDoor.setFill ('Saddle Brown')
frontDoor.draw(win)

sunCenter = g.Point(50, 50)
sunCircle = g.Circle(sunCenter, 15)
sunCircle.setFill ('yellow')
sunCircle.setOutline('yellow')
sunCircle.draw(win)

centerRoofPoint = g.Point(200,50)

doorDetail = g.Rectangle(g.Point(185,225),g.Point(215,310))
doorDetail.draw(win)


triangleRoof = g.Polygon(centerRoofPoint,g.Point(100,125),g.Point(300,125))
triangleRoof.setFill('Dark Slate Gray')
triangleRoof.draw(win)


lawn = g.Rectangle(g.Point(0,300), g.Point(400,400))
lawn.setFill('Lawn Green')
lawn.draw(win)
 

nightMessage = g.Text(g.Point(200,315), "Click here to change day to night")
nightMessage.setTextColor('Black')
nightMessage.setStyle('bold')
nightMessage.setSize(16)
nightMessage.draw(win)

win.getMouse()

for i in range(60):  # animate sun down below horizon
    sunCircle.move(0, 5)
    nightMessage.setTextColor('Lawn Green')
    g.time.sleep(.10)

for i in range(50):  # animate moon into sky with black background
    sunCircle.move(0, -5)
    sunCircle.setFill('White')
    sunCircle.setOutline('White')
    blueSky.setFill('Black')
    g.time.sleep(.10)
    
    
closeMessage = g.Text(g.Point(200,350), "Good Night!\nClick the screen to close it out")
closeMessage.setTextColor('Blue')
closeMessage.setStyle('bold')
closeMessage.setSize(16)
closeMessage.draw(win)

win.getMouse()
win.close()