import time
import board
import neopixel

currRed = 255
currGreen = 255
currBlue = 255
currBrightness = 255
currColorString = "255,255,255"

pixels = neopixel.NeoPixel(board.D27, 84, pixel_order=neopixel.GRBW, brightness=0.9)
pixels.fill((255, 255, 255))
pixels.fill((0, 0, 0))

def setColor(color):
#     print("using {}".format(colorString))
    firstCommaIndex = color.find(',')
    secondCommaIndex = color.rfind(',')

    red = color[0:firstCommaIndex]
    green = color[firstCommaIndex + 1:secondCommaIndex]
    blue = color[secondCommaIndex + 1:len(color)]
    pixels.fill((int(red), int(green), int(blue)))
    print("{}, {}, {}".format(red, green, blue))
    currRed = int(red)
    currGreen = int(green)
    currBlue = int(blue)

def setBrightness(brightness):
    print("Setting brightness to {}".format(brightness))
    global currBrightness
    brightness = float(brightness)
    stepCount = 20
    stepSize = (brightness - currBrightness) / stepCount
    print(stepSize)
    newBrightness = currBrightness
    for i in range(stepCount - 1):
        newBrightness = newBrightness + stepSize
        print(newBrightness)
        pixels.brightness = newBrightness / 255
        pixels.show()
        time.sleep(.01)
    pixels.brightness = brightness / 255
    currBrightness = brightness

