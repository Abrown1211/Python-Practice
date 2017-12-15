# You should probably start by copying and pasting the contents of
# your original my-house.py file into this one.

import graphics as g


def drawRectangle(rectShape, color,windowWidth,windowHeight,win):
    #rectShape = g.Rectangle(g.Point(0,0), g.Point(400,300))
    rectShape.setFill(color)
    rectShape.draw(win)
    return rectShape

def userMessage(screenMessage,color,style,textSize,windowWidth,windowHeight, win):
    screenMessage = g.Text(g.Point(200,350), "Good Night!\nClick the screen to close it out")
    screenMessage.setTextColor(color)
    screenMessage.setStyle(style)
    screenMessage.setSize(textSize)
    screenMessage.draw(win)
    return screenMessage

def drawRoof(color, windowWidth,windowHeight, win):
    centerRoofPoint = g.Point(200,50)
    triangleRoof = g.Polygon(centerRoofPoint,g.Point(100,125),g.Point(300,125))
    triangleRoof.setFill(color)
    triangleRoof.draw(win)
    return triangleRoof

def nightStars(starCircle,win):
    #starCenter = g.Point(50, 50)
    #starCircle = g.Circle(starCircle, 5)
    starCircle.setFill ('white')
    starCircle.setOutline('white')
    starCircle.draw(win)
            
def main():
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400

    win = g.GraphWin('My House', WINDOW_WIDTH, WINDOW_HEIGHT)
    
    
    #draws the background sky blue
    blueSky = g.Rectangle(g.Point(0,0), g.Point(400,300))
    blueSky.setFill('Light Sky Blue')
    blueSky.draw(win)
    
    #draws the sun and moon
    sunCenter = g.Point(50, 50)
    sunCircle = g.Circle(sunCenter, 15)
    sunCircle.setFill ('yellow')
    sunCircle.setOutline('yellow')
    sunCircle.draw(win)
    
    #draws the roof of the house with any color selection
    drawRoof("Dark Slate Gray", WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the outline of the house
    drawRectangle(g.Rectangle(g.Point(100,125), g.Point (300, 300)), "Indian Red",WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the left window of the house
    drawRectangle(g.Rectangle(g.Point(130,220), g.Point (150, 250)), "Light Gray", WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the right window of the house
    drawRectangle(g.Rectangle(g.Point(250,220), g.Point (270, 250)),"Light Gray", WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the front door of the house
    drawRectangle(g.Rectangle(g.Point(180,220), g.Point (220, 300)), "Saddle Brown",WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the inside of the door detail
    drawRectangle(g.Rectangle(g.Point(185,225),g.Point(215,300)), "Saddle Brown", WINDOW_WIDTH,WINDOW_HEIGHT, win)
    #draws the grass surrounding the house
    drawRectangle(g.Rectangle(g.Point(0,300), g.Point(400,400)), "Lawn Green", WINDOW_WIDTH,WINDOW_HEIGHT, win)

    
    userMessage("Click here to change day to night","Black",'bold',16,WINDOW_WIDTH,WINDOW_HEIGHT, win)
    
    win.getMouse()

    for i in range(60):  # animate sun down below horizon
        sunCircle.move(0, 5)
        userMessage("Click here to change day to night","Lawn Green",'bold',16,WINDOW_WIDTH,WINDOW_HEIGHT, win)
        g.time.sleep(.10)

    for i in range(50):  # animate moon into sky with black background
        sunCircle.move(0, -5)
        sunCircle.setFill('White')
        sunCircle.setOutline('White')
        blueSky.setFill('Black')
        g.time.sleep(.10)
    
    nightStars(g.Circle(g.Point(100,60), 5),win)
    nightStars(g.Circle(g.Point(250,50), 5),win)
    nightStars(g.Circle(g.Point(350,150), 5),win)
 
    userMessage("Good Night!\nClick the screen to close it out","Blue",'bold',16, WINDOW_WIDTH,WINDOW_HEIGHT, win)  

    win.getMouse()
    win.close()
    
main()