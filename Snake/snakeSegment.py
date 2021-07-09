from graphics import *

class snakeSegment:
    segment = Rectangle(Point(0,0), Point(0,0))
    segP1 = Point(0,0)
    segP2 = Point(0,0)
    segDirection = "right"
    segLength = 0

    def __init__(self, p1, p2, direction, length):
        self.segP1 = p1
        self.segP2 = p2
        self.segDirection = direction
        self.segLength = length

        self.segment = Rectangle(p1, p2)
        self.segment.setFill("green")
        self.segment.setOutline("green")

    def shrinkSegment():
        if segDirection == "right":
            segP1 = Point(segP1.getX() + 2, segP1.getY())
        elif segDirection == "left":
            segP2 = Point(segP2.getX() - 2, segP2.getY())
        elif segDirection == "up":
            segP1 = Point(segP1.getX(), segP1.getY() + 2)
        elif segDirection == "right":
            segP2 = Point(segP2.getX(), segP2.getY() - 2)