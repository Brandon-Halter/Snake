from graphics import *
from pynput import keyboard
import time
import random
from snakeSegment import snakeSegment

#Create global variables
initialSegment = snakeSegment(Point(380,395), Point(420,405), "right", 40)
growthPellet = Rectangle(Point(600, 600), Point(608, 608))
growthPellet.setFill("black")
segments = [initialSegment]
win = GraphWin("gameWindow", 800, 800, autoflush=False)
runGame = True
direction = 'right'


#=================================================================================================

#Define behavior for keyboard listener
def on_press(key):
	global runGame
	global direction

	try:
		if key == keyboard.Key.esc:
			runGame = False
			return False
		elif key.char == 'd' and direction != "left" and direction != "right":
			addSegment()
			segments[0].segDirection = "right"
			segments[0].turnSegment(direction)
			direction = 'right'
		elif key.char == 'a' and direction != "left" and direction != "right":
			addSegment()
			segments[0].segDirection = "left"
			segments[0].turnSegment(direction)
			direction = 'left'
		elif key.char == 'w' and direction != "up" and direction != "down":
			addSegment()
			segments[0].segDirection = "up"
			segments[0].turnSegment(direction)
			direction = 'up'
		elif key.char == 's' and direction != "up" and direction != "down":
			addSegment()
			segments[0].segDirection = "down"
			segments[0].turnSegment(direction)
			direction = 'down'

	except:
		pass

#=================================================================================================

def clearWindow(win):
	for item in win.items[:]:
		item.undraw()


def redrawWindow(win, segments):
	try:
		for segment in segments:
			segment.segment.draw(win)
		growthPellet.draw(win)
		win.update()
	except:
		pass

#=================================================================================================

listener = keyboard.Listener(on_press=on_press)

#=================================================================================================

#Check if pellet and snake overlap. If they do move pellet
def pelletHitDetection():
	global growthPellet

	xBoundOne = int(segments[0].segP1.getX())
	xBoundTwo = int(segments[0].segP2.getX())
	yBoundOne = int(segments[0].segP1.getY())
	yBoundTwo = int(segments[0].segP2.getY())
	pelletX1 = int(growthPellet.getP1().getX())
	pelletX2 = int(growthPellet.getP2().getX())
	pelletY1 = int(growthPellet.getP1().getY())
	pelletY2 = int(growthPellet.getP2().getY())

	if ((pelletX1 in range(xBoundOne, xBoundTwo + 1)) and (pelletY1 in range(yBoundOne, yBoundTwo + 1))) or ((pelletX1 in range(xBoundTwo, xBoundOne + 1)) and (pelletY1 in range(yBoundTwo, yBoundOne + 1))):
		newX = random.randint(20, 700)
		newY = random.randint(20, 700)
		growthPellet = Rectangle(Point(newX, newY), Point(newX + 8, newY + 8))
		growthPellet.setFill("black")
		segments[0].growSegment(direction)
	elif ((pelletX2 in range(xBoundOne, xBoundTwo + 1)) and (pelletY2 in range(yBoundOne, yBoundTwo + 1))) or ((pelletX2 in range(xBoundTwo, xBoundOne + 1)) and (pelletY2 in range(yBoundTwo, yBoundOne + 1))):
		newX = random.randint(20, 700)
		newY = random.randint(20, 700)
		growthPellet = Rectangle(Point(newX, newY), Point(newX + 8, newY + 8))
		growthPellet.setFill("black")
		segments[0].growSegment(direction)
#=================================================================================================

#Draw initial window
def initialize():
	(initialSegment.segment).draw(win)
	growthPellet.draw(win)
	win.update()

#Run the game
def runGame():
	listener.start()

	while(runGame):
		moveSnake(direction)
		pelletHitDetection()

#=================================================================================================

#Make the snake respond to movement inputs
def moveSnake(direction):
	time.sleep(.001)

	#Remove end of snake
	lastSegment = segments[len(segments) - 1]
	lastSegment.shrinkSegment()

	#Check if last segment is completely gone
	if lastSegment.segLength <= 0:
		segments.pop(len(segments) - 1)

	#Add front of snake
	firstSegment = segments[0]
	firstSegment.growSegment(direction)



	clearWindow(win)
	redrawWindow(win, segments)

#=================================================================================================
#This function adds a trailing segment in the snake
def addSegment():
	centerPoint = segments[0].segment.getCenter()
	newLength = segments[0].segLength - 20

	#Caclulate segment coordinates
	if direction == "up":
		P1 = Point(centerPoint.getX() + 5, centerPoint.getY() - segments[0].segLength/2)
		P2 = Point(P1.getX() - 10, P1.getY() + segments[0].segLength - 1)
	elif direction == "down":
		P1 = Point(centerPoint.getX() + 5, centerPoint.getY() + segments[0].segLength/2)
		P2 = Point(P1.getX() - 10, P1.getY() - segments[0].segLength + 1)
	elif direction == "right":
		P1 = Point(centerPoint.getX()  + segments[0].segLength/2, centerPoint.getY() - 5)
		P2 = Point(P1.getX() - segments[0].segLength + 1, P1.getY() + 10)
	elif direction == "left":
		P1 = Point(centerPoint.getX()  - segments[0].segLength/2, centerPoint.getY() - 5)
		P2 = Point(P1.getX() + segments[0].segLength - 1, P1.getY() + 10)

	#Add new segment
	segments.insert(1, snakeSegment(P1, P2, direction, newLength))
#=================================================================================================

def main():
	initialize()

	runGame()

main()
