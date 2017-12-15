from button import Button
from die_view import DieView
from sum_counter_view import *
from graphics import *

def main():
    win = GraphWin("Double Die Roller", 500, 300)
    win.setBackground( 'dark green' )
    dieView1 = DieView( win, Point( 60, 80 ), 100 )
    dieView2 = DieView( win, Point( 175, 80 ), 100 )
    
    counter_views = {
        7: SumCounter( win, Point( 375, 50), 160, 50, 7),
        8: SumCounter( win, Point( 375, 115), 160, 50, 8),
        9: SumCounter( win, Point( 375, 180), 160, 50, 9),
        10: SumCounter( win, Point( 375, 245), 160, 50, 10)
    }
    
    rollButton = Button( win, Point( 120, 180), 100, 40, "Roll!" )
   
    while True:
        mouseClick = win.getMouse()
        if rollButton.wasClickedIn( mouseClick ):
            dieView1.roll()
            dieView2.roll()
            sum = dieView1.getValue() + dieView2.getValue()
            
            if sum in counter_views:
                counter_views[sum].handleRoll()
                counter_views[sum].setText()
    
main()