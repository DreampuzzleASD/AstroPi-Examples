from gpiozero import Button
from sense_hat import SenseHat

A = Button(16)
B = Button(21)
UP = Button(26)
DOWN = Button(13)
LEFT = Button(20)
RIGHT = Button(19)

sense = SenseHat()