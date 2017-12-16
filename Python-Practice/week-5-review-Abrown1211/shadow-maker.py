from graphics import *


def makeShadow(shape,win):
    if shape == "c":
        c = Circle( Point( 44, 79 ), 30 )
        c.setOutline( 'light gray' )
        c.setFill( 'light gray' )
        c.draw( win )
    else:
        r = Rectangle( Point( 84, 34 ), Point( 144, 144 ))
        r.setFill( 'light gray' )
        r.setOutline( 'light gray' )
        r.draw( win )
    return shape
            
#makeShadow("c")

def drawCircle(color,win):
    c = Circle( Point( 40, 75 ), 30 )
    ColorFill = c.setFill( color)
    Outline = c.setOutline( color )
    c.draw( win )
    return c
    
def drawRectangle(color, win):
    r = Rectangle( Point( 80, 30 ), Point( 140, 140 ))
    ColorFill = r.setFill( color )
    Outline = r.setOutline( color )
    r.draw( win )
    return r
    
def testShadowMaker():
   #draws the main graphical window to display the graph objects.
    win = GraphWin()
    
    """draws two shadows one behind each original shape offset by 4 pixels,
    takes a shape parameter "c" for circle or "r" for rectangle."""
    makeShadow("r",win)
    makeShadow("c",win)
    
    #draws the original shapes to overlay on top of shadowMaker shapes. Accepts a color parameter for the shape.
    drawCircle("blue",win)
    drawRectangle("orange",win)
    
    #Gets user mouse to close the graphical window
    win.getMouse()
    win.close()
    
testShadowMaker()
