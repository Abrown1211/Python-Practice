#creates a file with random shape points written to it.

from random import *
from graphics import *

def userFileInput():
    fileName = input("Enter the drawing file name to create: ")
    shapeCount = int(input("Enter the number of shapes to make: "))
    fileName = open(fileName, "w")
    return fileName, shapeCount

def randomShape():
    if random() < .5:
        shapeChoice = "rectangle"
    else:
        shapeChoice = "circle"
    return shapeChoice

def shapeColorGenerator():
    r = randrange(50,225)
    b = randrange(25,256)
    g = randrange(55,240)
    color = color_rgb(r, g, b)
    return color

def getRectangle( fileName, color ):
    x1 = randint(5,440)
    y1 = randint(5,440)
    uprLftPt = x1,y1
    x2 = x1 + randrange(20,440)
    y2 = y1 + randrange(20,440)
    lwrRghtPt = x2,y2
    color = shapeColorGenerator()
    rectangleWrite = print("rectangle;{0};{1};{2}".format( uprLftPt,lwrRghtPt,color), file= fileName)
    return rectangleWrite
        
        
def getCircle( fileName, color ):
    radius = randrange(3, 20)
    x = randrange(5, 395)
    y = randrange(5, 395)
    centerPt = x,y
    color = shapeColorGenerator()
    circleWrite = print("circle;{0};{1};{2}".format( centerPt, radius,color), file=fileName)
    return circleWrite

def shapeGenerator( shapeCount, fileName, color ):
    for shapes in range(shapeCount):
        shapeChoice = randomShape()
        if shapeChoice == "rectangle":
            shapes = getRectangle( fileName, color)
        else:
            shapes = getCircle( fileName, color )
        return shapes
              
                    
def main():
    fileName, shapeCount = userFileInput()
    color = shapeColorGenerator()
    for shapes in range(shapeCount):
        shapeChoice = randomShape()
        if shapeChoice == "rectangle":
            shapes = getRectangle( fileName, color)
        else:
            shapes = getCircle( fileName, color )
    fileName = fileName.close()
    print ("Your file has been processed successfully!")
    
main()

    
    