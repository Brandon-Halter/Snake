from graphics import *
from pynput import keyboard
import time
import snakeSegment

#Create global variables
test = "test"
snake = Rectangle(Point(380,395), Point(420,405))
win = GraphWin("My Circle", 800, 800)
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
			direction = 'right'
		elif key.char == 'a':
			direction = 'left'
		elif key.char == 'w':
			direction = 'up'
		elif key.char == 's':
			direction = 'down'

	except AttributeError:
		pass



listener = keyboard.Listener(on_press=on_press)


#Draw initial window
def initialize():
	snake.setFill("green")
	snake.setOutline("green")
	snake.draw(win)

#Run the game
def runGame():
	listener.start()

	while(runGame):
		moveSnake(direction)

#Make the snake respond to movement inputs
def moveSnake(direction):
	time.sleep(.001)
	if direction == 'up':
		snake.move(0, -2)
	elif direction == 'down':
		snake.move(0, 2)
	elif direction == 'left':
		snake.move(-2, 0)
	elif direction == 'right':
		snake.move(2, 0)


def main():
	initialize()

	runGame()

main()
