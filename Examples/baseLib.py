from gpiozero import Button
from sense_hat import SenseHat

A = Button(16)
B = Button(21)
UP = Button(26)
DOWN = Button(13)
LEFT = Button(20)
RIGHT = Button(19)

sense = SenseHat()

R = [255, 0, 0]
G = [0, 255, 0]
W = [255, 255, 255]


def redCross():
    redCross = [
        R, W, W, W, W, W, W, R,
        W, R, W, W, W, W, R, W,
        W, W, R, W, W, R, W, W,
        W, W, W, R, R, W, W, W,
        W, W, W, R, R, W, W, W,
        W, W, R, W, W, R, W, W,
        W, R, W, W, W, W, R, W,
        R, W, W, W, W, W, W, R
    ]
    sense.set_pixels(redCross)


def greenTick():
    greenTick = [
        W, W, W, W, W, W, W, G,
        W, W, W, W, W, W, W, G,
        W, W, W, W, W, W, G, W,
        W, W, W, W, W, W, G, W,
        W, W, W, W, W, G, W, W,
        G, W, W, W, W, G, W, W,
        W, G, W, W, G, W, W, W,
        W, W, G, G, W, W, W, W
    ]
    sense.set_pixels(greenTick)


def white():
    white = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W
    ]
    sense.set_pixels(white)


def showText(text):
    sense.show_message(str(text))


def getTemperature():
    return sense.get_temperature()


def getHuminidty():
    return sense.get_humidity()
