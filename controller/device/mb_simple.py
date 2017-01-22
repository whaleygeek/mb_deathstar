from microbit import *

while True:
    sleep(100)
    if accelerometer.get_x() < -500:    print("L")
    if accelerometer.get_x() > 500:     print("R")
    if accelerometer.get_y() < -500:    print("D")
    if accelerometer.get_y() > 500:     print("U")
    if button_a.is_pressed():           print("A")
    if button_b.is_pressed():           print("B")

    