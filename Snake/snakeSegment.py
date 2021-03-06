from graphics import *

class snakeSegment:
    segment = Rectangle(Point(0,0), Point(0,0))
    segP1 = Point(0,0)
    segP2 = Point(0,0)
    segDirection = "right"
    segLength = 0

#=================================================================================================

    def __init__(self, p1, p2, direction, length):
        self.segP1 = p1
        self.segP2 = p2
        self.segDirection = direction
        self.segLength = length

        self.segment = Rectangle(p1, p2)
        self.segment.setFill("green")
        self.segment.setOutline("green")

#=================================================================================================

    def shrinkSegment(self):
        #Change coordinates
        if self.segDirection == "right":
            #Check to see if P1 or P2 is trailing edge
            if self.segP1.getX() < self.segP2.getX():
                self.segP1 = Point(self.segP1.getX() + 2, self.segP1.getY()) 
            else:
                self.segP2 = Point(self.segP2.getX() + 2, self.segP2.getY()) 
        elif self.segDirection == "left":
            #Check to see if P1 or P2 is trailing edge
            if self.segP1.getX() < self.segP2.getX():
                self.segP2 = Point(self.segP2.getX() - 2, self.segP2.getY())
            else:
                self.segP1 = Point(self.segP1.getX() - 2, self.segP1.getY())
        elif self.segDirection == "up":
            #Check to see if P1 or P2 is trailing edge
            if self.segP1.getY() > self.segP2.getY():
                self.segP1 = Point(self.segP1.getX(), self.segP1.getY() - 2)
            else:
                self.segP2 = Point(self.segP2.getX(), self.segP2.getY() - 2)
        elif self.segDirection == "down":
            #Check to see if P1 or P2 is trailing edge
            if self.segP1.getY() > self.segP2.getY():
                self.segP2 = Point(self.segP2.getX(), self.segP2.getY() + 2)
            else:
                self.segP1 = Point(self.segP1.getX(), self.segP1.getY() + 2)
        self.segLength = self.segLength - 2

        #Update segment with new coordinates
        self.segment = Rectangle(self.segP1, self.segP2)
        self.segment.setFill("green")
        self.segment.setOutline("green")

#=================================================================================================

    def growSegment(self, direction, amount):
        #Change coordinates
        if direction == "right":
            #Check to see if P1 or P2 is leading edge
            if self.segP1.getX() > self.segP2.getX():
                self.segP1 = Point(self.segP1.getX() + amount, self.segP1.getY())
            else:
                self.segP2 = Point(self.segP2.getX() + amount, self.segP2.getY())
        elif direction == "left":
            #Check to see if P1 or P2 is leading edge
            if self.segP1.getX() < self.segP2.getX():
                self.segP1 = Point(self.segP1.getX() - amount, self.segP1.getY())
            else:
                self.segP2 = Point(self.segP2.getX() - amount, self.segP2.getY())
        elif direction == "up":
            #Check to see if P1 or P2 is leading edge
            if self.segP1.getY() < self.segP2.getY():
                self.segP1 = Point(self.segP1.getX(), self.segP1.getY() - amount)
            else:
                self.segP2 = Point(self.segP2.getX(), self.segP2.getY() - amount)
        elif direction == "down":
            #Check to see if P1 or P2 is leading edge
            if self.segP1.getY() < self.segP2.getY():
                self.segP2 = Point(self.segP2.getX(), self.segP2.getY() + amount)
            else:
                self.segP1 = Point(self.segP1.getX(), self.segP1.getY() + amount)

        self.segLength = self.segLength + amount

        #Update segment with new coordinates
        self.segment = Rectangle(self.segP1, self.segP2)
        self.segment.setFill("green")
        self.segment.setOutline("green")

#=================================================================================================

    def turnSegment(self, prevDirection):
        if self.segDirection == "right":
            #Calculate coordinates after turn and update height
            currentLocation = self.segment.getCenter()
            if prevDirection == "down":
                self.segP1 = Point(currentLocation.getX() - 5, currentLocation.getY() + self.segLength/2)
                self.segP2 = Point(self.segP1.getX() + 10, self.segP1.getY() + 10)
            elif prevDirection == "up":
                self.segP1 = Point(currentLocation.getX() - 5, currentLocation.getY() - self.segLength/2)
                self.segP2 = Point(self.segP1.getX() + 10, self.segP1.getY() - 10)
            self.segLength = 10
        elif self.segDirection == "left":
            #Calculate coordinates after turn and update height
            currentLocation = self.segment.getCenter()
            if prevDirection == "down":
                self.segP1 = Point(currentLocation.getX() + 5, currentLocation.getY() + self.segLength/2)
                self.segP2 = Point(self.segP1.getX() - 10, self.segP1.getY() + 10)
            elif prevDirection == "up":
                self.segP1 = Point(currentLocation.getX() + 5, currentLocation.getY() - self.segLength/2)
                self.segP2 = Point(self.segP1.getX() - 10, self.segP1.getY() - 10)
            self.segLength = 10
        elif self.segDirection == "up":
            #Calculate coordinates after turn and update height
            currentLocation = self.segment.getCenter()
            if prevDirection == "left":
                self.segP1 = Point(currentLocation.getX() - self.segLength/2, currentLocation.getY() + 5)
                self.segP2 = Point(self.segP1.getX() + 10, self.segP1.getY() - 10)
            elif prevDirection == "right":
                self.segP1 = Point(currentLocation.getX() + self.segLength/2, currentLocation.getY() + 5)
                self.segP2 = Point(self.segP1.getX() - 10, self.segP1.getY() - 10)
            self.segLength = 10
        elif self.segDirection == "down":
            #Calculate coordinates after turn and update height
            currentLocation = self.segment.getCenter()
            if prevDirection == "left":
                self.segP1 = Point(currentLocation.getX() - self.segLength/2, currentLocation.getY() - 5)
                self.segP2 = Point(self.segP1.getX() + 10, self.segP1.getY() + 10)
            elif prevDirection == "right":
                self.segP1 = Point(currentLocation.getX() + self.segLength/2, currentLocation.getY() - 5)
                self.segP2 = Point(self.segP1.getX() - 10, self.segP1.getY() + 10)
            self.segLength = 10