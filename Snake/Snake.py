from graphics import *
from pynput import keyboard
import time
from snakeSegment import snakeSegment

#Create global variables
initialSegment = snakeSegment(Point(380,395), Point(420,405), "right", 40)
segments = [initialSegment]
win = GraphWin("gameWindow", 800, 800, autoflush=False)
runGame = True
direction = 'right'

#Define behavior for keyboard listener
def on_press(key):
	global runGame
	global direction

	try:
		if key == keyboard.Key.esc:
			runGame = False
			return False
		elif key.char == 'd' and direction != "left" and direction != "right":
			segments.append(snakeSegment(Point(200, 200), Point(210,220), direction, 20))
			segments[0].segDirection = "right"
			segments[0].turnSegment(direction)
			direction = 'right'
		elif key.char == 'a' and direction != "left" and direction != "right":
			segments.append(snakeSegment(Point(200, 200), Point(210,220), direction, 20))
			segments[0].segDirection = "left"
			segments[0].turnSegment(direction)
			direction = 'left'
		elif key.char == 'w' and direction != "up" and direction != "down":
			segments.append(snakeSegment(Point(200, 200), Point(220,210), direction, 20))
			segments[0].segDirection = "up"
			segments[0].turnSegment(direction)
			direction = 'up'
		elif key.char == 's' and direction != "up" and direction != "down":
			segments.append(snakeSegment(Point(200, 200), Point(220,210), direction, 20))
			segments[0].segDirection = "down"
			segments[0].turnSegment(direction)
			direction = 'down'

	except:
		pass

def clearWindow(win):
	for item in win.items[:]:
		item.undraw()


def redrawWindow(win, segments):
	for segment in segments:
		segment.segment.draw(win)
	win.update()



listener = keyboard.Listener(on_press=on_press)


#Draw initial window
def initialize():
	(initialSegment.segment).draw(win)
	win.update()

#Run the game
def runGame():
	listener.start()

	while(runGame):
		for s in segments:
			moveSnake(direction)

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


def main():
	initialize()

	runGame()

main()
