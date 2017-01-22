from microbit import *

def fly():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    
    if a: print("A")
    if b: print("B")
    if x < -500: print("L")
    if x > 500:  print("R")
    if y < -500: print("D")
    if y > 500:  print("U")

def run():
    while True:
        display.set_pixel(2,2,9)
        fly()
        sleep(100)
        display.set_pixel(2,2,0)
        fly()
        sleep(100)
run()
