from graphics import *

from msdie import MultiSidedDie

class SumCounter:
    
    def __init__( self, window, centerPt, width, height, targetValue):
        self.minX = centerPt.getX() - width / 2.0
        self.maxX = centerPt.getX() + width / 2.0
        
        self.minY = centerPt.getY() - height / 2.0
        self.maxY = centerPt.getY() + height / 2.0
        
        ulPt = Point( self.minX, self.minY)
        lrPt = Point( self.maxX, self.maxY)
        
        self.rect = Rectangle( ulPt, lrPt )
        self.rect.setFill( 'white' )
        self.rect.draw( window )
        
        self.text = Text( centerPt, "")
        self.text.draw( window )
        self.targetValue = targetValue
        self.targetValueCount = 0
        
        self.setText()
    def setText(self):
        self.text.setText("Total of {value}:{valueCount} times".format(
            value=self.targetValue,
            valueCount=self.targetValueCount
            )
        )
    def handleRoll( self):
        self.targetValueCount += 1
        