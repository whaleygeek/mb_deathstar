from microbit import *

UPDATES_PER_SEC = 10
DELAY_MS        = 1000/UPDATES_PER_SEC

def fly():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    a = button_a.is_pressed()
    b = button_b.is_pressed()

    m = ""
    if a:           m += 'A'
    if b:           m += 'B'
    if x < -500:    m += 'L'
    if x > 500:     m += 'R'
    if y < -500:    m += 'D'
    if y > 500:     m += 'U'
    if len(m) > 0:  print(m)

brightness = 0
def flash():
    """flash the middle pixel of the display"""
    global brightness
    display.set_pixel(2, 2, brightness)
    if brightness == 0:
        brightness = 9
    else:
        brightness = 0

def run():
    while True:
        fly()
        flash()
        sleep(DELAY_MS)

run()
