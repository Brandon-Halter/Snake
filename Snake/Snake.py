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
win = GraphWin("Snake", 800, 800, autoflush=False)
runGame = True
direction = 'right'
score = 0
counter = Text(Point(750, 30), "Score: " + str(score))

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
		counter.draw(win)

		win.update()
	except:
		pass

#=================================================================================================

listener = keyboard.Listener(on_press=on_press)

#=================================================================================================

def inRange(point, boundOne, boundTwo):
	if (point < boundOne and point > boundTwo) or (point > boundOne and point < boundTwo):
		return True
	else:
		return False

#=================================================================================================

#Check if pellet and snake overlap. If they do move pellet
def pelletHitDetection():
	global growthPellet
	global score

	xBoundOne = (segments[0].segP1.getX())
	xBoundTwo = (segments[0].segP2.getX())
	yBoundOne = (segments[0].segP1.getY())
	yBoundTwo = (segments[0].segP2.getY())
	pelletX1 = (growthPellet.getP1().getX())
	pelletX2 = (growthPellet.getP2().getX())
	pelletY1 = (growthPellet.getP1().getY())
	pelletY2 = (growthPellet.getP2().getY())

	if (inRange(pelletX1, xBoundOne, xBoundTwo)) and (inRange(pelletY1, yBoundOne, yBoundTwo)):
		#Redraw pellet
		newX = random.randint(20, 700)
		newY = random.randint(20, 700)
		growthPellet = Rectangle(Point(newX, newY), Point(newX + 8, newY + 8))
		growthPellet.setFill("black")
		#Grow snake
		segments[0].growSegment(direction)
		#Add score
		score = score + 1
		counter.setText("Score: " + str(score))
	elif (inRange(pelletX2, xBoundOne, xBoundTwo)) and (inRange(pelletY2, yBoundOne, yBoundTwo)):
		#Redraw pellet
		newX = random.randint(20, 700)
		newY = random.randint(20, 700)
		growthPellet = Rectangle(Point(newX, newY), Point(newX + 8, newY + 8))
		growthPellet.setFill("black")
		#Grow snake
		segments[0].growSegment(direction)
		#Add score
		score = score + 1
		counter.setText("Score: " + str(score))

#=================================================================================================

def deathDetection():
	global runGame

	#Get coordinates of snake head
	headX1 = segments[0].segP1.getX()
	headX2 = segments[0].segP2.getX()
	headY1 = segments[0].segP1.getY()
	headY2 = segments[0].segP2.getY()

	#Loop trough snake segments
	for i in range(1, len(segments) - 1):
		segX1 = segments[i].segP1.getX()
		segX2 = segments[i].segP2.getX()
		segY1 = segments[i].segP1.getY()
		segY2 = segments[i].segP2.getY()

		if (inRange(headX1, segX1, segX2)) and (inRange(headY1, segY1, segY2)):
			runGame = False
		elif (inRange(headX2, segX1, segX2)) and (inRange(headY2, segY1, segY2)):
			runGame = False
#=================================================================================================

#Draw initial window
def initialize():
	(initialSegment.segment).draw(win)
	growthPellet.draw(win)
	counter.draw(win)
	win.update()

#Run the game
def runGame():
	listener.start()

	while(runGame):
		moveSnake(direction)
		pelletHitDetection()
		deathDetection()

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
