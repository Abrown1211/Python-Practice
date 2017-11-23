from graphics import *

def endPoints(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1

def insidePoints(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return endPoints(point.getX(), pt1.getX(), pt2.getX()) and \
           endPoints(point.getY(), pt1.getY(), pt2.getY())

def polyDraw(rect, win):
    rect.setOutline("red")
    rect.draw(win)
    vertices = list()
    pt = win.getMouse()
    while insidePoints(pt, rect):
        vertices.append(pt) 
        poly = Polygon(vertices)  
        poly.draw(win)
        pt = win.getMouse()
        poly.undraw() 
    poly.draw(win)
    rect.undraw()
    return poly

def main():
    winWidth = 400
    winHeight = 400
    win = GraphWin('Drawing Polygons', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight) 
    
    instructions = Text(Point(winWidth/2, 30),
                        "Click vertices inside the red rectangle."+
                        "\nClick outside the rectangle to stop.")
    instructions.draw(win)

    rect1 = Rectangle(Point(25, 55), Point(350, 300))
    poly1 = polyDraw(rect1, win)
    win.getMouse()
    win.close()

main()