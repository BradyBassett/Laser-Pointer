add_library('serial')
import time

side = 900
hSide = side / 2
port = Serial(this, Serial.list()[1], 9600)

def setup():
    size(900,900)
    frameRate(100)
    port.bufferUntil(10)
    
def draw():
    fill(51)
    rect(0,0,side,side)
    fill(255,0,0)
    rect(hSide, hSide - 5, mouseX-hSide, 10)
    fill(0,255,0)
    rect(hSide -5, hSide, 10, mouseY-hSide)
    
    update(mouseX, mouseY)

def update(x, y):
    time.sleep(.015)
    serialData = "X{0}Y{1}"
    port.write(serialData.format((x / (side / 180)), (y / (side / 180))))
    
    print("X{0}Y{1}".format((x / (side / 180)), (y / (side / 180))))
