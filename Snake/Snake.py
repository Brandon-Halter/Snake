from graphics import *
import time
from pynput import keyboard

test = "test"
snake = Rectangle(Point(380,395), Point(420,405))
win = GraphWin("My Circle", 800, 800)
runGame = True
direction = 'right'

def on_press(key):
	global runGame
	global direction

	#Set movement direction and check for escape key
	if key.char == 'd':
		direction = 'right'
	elif key.char == 'a':
		direction = 'left'
	elif key.char == 'w':
		direction = 'up'
	elif key.char == 's':
		direction = 'down'
	elif key == keyboard.Key.esc:
		runGame = False
		return False


listener = keyboard.Listener(on_press=on_press)


def main():
	initialize()

	runGame()





def initialize():
	#Draw snake
	snake.setFill("green")
	snake.setOutline("green")
	snake.draw(win)


def runGame():
	listener.start()

	while(runGame):
		moveSnake(direction)

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

main()
