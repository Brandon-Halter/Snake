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
		elif key.char == 'd':
			segments.append(snakeSegment(Point(200, 200), Point(220,240), direction, 40))
			direction = 'right'
			segments[0].segDirection = direction
		elif key.char == 'a':
			segments.append(snakeSegment(Point(200, 200), Point(220,240), direction, 40))
			direction = 'left'
			segments[0].segDirection = direction
		elif key.char == 'w':
			segments.append(snakeSegment(Point(200, 200), Point(240,220), direction, 40))
			direction = 'up'
			segments[0].segDirection = direction
		elif key.char == 's':
			segments.append(snakeSegment(Point(200, 200), Point(240,220), direction, 40))
			direction = 'down'
			segments[0].segDirection = direction

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
