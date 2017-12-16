# Please do your work for problem four in this file

import graphics as g

win = g.GraphWin('Gradient Bar', 400,400)



def barOne():
    bar = g.Rectangle(g.Point(0,0), g.Point(66,400))
    bar.setFill(g.color_rgb(0,42,0))
    bar.setWidth(0)
    bar.draw(win)
    
def barTwo():
    bar = g.Rectangle(g.Point(66,0), g.Point(133,400))
    bar.setFill(g.color_rgb(0,84,0))
    bar.setWidth(0)
    bar.draw(win)
    
def barThree():
    bar = g.Rectangle(g.Point(133,0), g.Point(200,400))
    bar.setFill(g.color_rgb(0,127,0))
    bar.setWidth(0)
    bar.draw(win)
    
def barFour():
    bar = g.Rectangle(g.Point(200,0), g.Point(266,400))
    bar.setFill(g.color_rgb(0,169,0))
    bar.setWidth(0)
    bar.draw(win)
    
def barFive():
    bar = g.Rectangle(g.Point(266,0), g.Point(333,400))
    bar.setFill(g.color_rgb(0,212,0))
    bar.setWidth(0)
    bar.draw(win)
    
def barSix():
    bar = g.Rectangle(g.Point(333,0), g.Point(400,400))
    bar.setFill(g.color_rgb(0,255,0))
    bar.setWidth(0)
    bar.draw(win)
    

barOne()
barTwo()
barThree()
barFour()
barFive()
barSix()

clickPoint = win.getMouse()
win.close()