import baseLib
from time import sleep
from pynput import keyboard


def testButton(button):
    baseLib.redCross()
    button.wait_for_press()
    print("button press")
    baseLib.greenTick()
    sleep(2)

def testHat():
    temp = baseLib.getTemperature()
    humid = baseLib.getHuminidty()
    print("Test Temperature: " + str(temp))
    baseLib.showText(temp)
    sleep(2)
    print("Test Humidity: " + str(humid))
    baseLib.showText(humid)
    sleep(2)

def on_press(key):
    if key == keyboard.Key.enter:
        startTest()
    elif key == keyboard.Key.esc:
        print("exit...")
        exit(0)
    else:
        print("Press Enter to start test\nPress Esc to exit")


def startTest():
    print("Testing Hat Sensors")
    testHat()
    print("Now press buttons on AstroPi")
    print("Press A")
    testButton(baseLib.A)
    print("Press B")
    testButton(baseLib.B)
    print("Press UP")
    testButton(baseLib.UP)
    print("Press DOWN")
    testButton(baseLib.DOWN)
    print("Press LEFT")
    testButton(baseLib.LEFT)
    print("Press RIGHT")
    testButton(baseLib.RIGHT)
    print("Now test is concluded")
    baseLib.resetPixels()
    exit(0)


def __init__():
    print("Start test?\nPress Enter on keyboard\nEsc to exit")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()


__init__()



