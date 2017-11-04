import graphics as g

win = g.GraphWin( 'green', 300, 300 )
win.setBackground( g.color_rgb(int( 0), int(255), int(0)))

centerPoint = g.Point(150, 150)

firstBase = g.Rectangle( g.Point(200, 140), g.Point(215, 155))
firstBase.setFill( 'white' )
firstBase.draw( win )

secondBase = g.Rectangle( g.Point(140, 75), g.Point(155, 90))
secondBase.setFill( 'white' )
secondBase.draw( win )

thirdBase = g.Rectangle( g.Point(85, 140), g.Point(100, 155))
thirdBase.setFill( 'white' )
thirdBase.draw( win )

pitchersMound = g.Circle(centerPoint, 10)
pitchersMound.setFill( 'tan' )
pitchersMound.draw( win )

homeBase = g.Polygon( g.Point(140, 220), g.Point(160, 220), g.Point(150, 235))
homeBase.setFill( 'white' )
homeBase.draw( win )

firstBLine = g.Line( g.Point(160, 220), g.Point(300,50))
firstBLine.draw( win )

thirdBLine = g.Line( g.Point(140, 220), g.Point(0,50))
thirdBLine.draw( win )

clickPoint = win.getMouse()
win.close()
