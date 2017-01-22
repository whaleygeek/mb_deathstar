# pg_controller.py - a simple controller module using pygame keypress events

import pygame
##import thread
##import atexit
import time

##def start():
##    pass #TODO:
##    # start a thread that calls tick() regularly
##    atexit.register(stop)

##def tick():
##    pass #TODO:

##def stop():
##    pass #TODO:
##    # stop the ticker thread

commands = {
    pygame.K_LEFT:  'L',
    pygame.K_RIGHT: 'R',
    pygame.K_UP:    'U',
    pygame.K_DOWN:  'D',
    pygame.K_A:     'A',
    pygame.K_B:     'B'
}
keys = []

def get_command_flags():
    """Get a collection of flags, one for each possible button/action"""
    global idx

    # Process all queued keypresses and keyreleases, in order
    # and update the 'keys' list
    for event in pygame.events.get():
        if event.type == pygame.KEYDOWN:
            try:
                letter = commands[event.key]
                if not letter in keys:
                    keys.append(letter)
            except:
                pass # ignore unknown key presses

        elif event.type == pygame.KEYUP:
            try:
                letter = commands[event.key]
                if letter in keys:
                    keys.remove(letter)
            except:
                pass # ignore unknown key releases

    return keys


# auto-start the keyboard monitor thread when module is imported
#start()

#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__": # test harness
    while True:
        time.sleep(0.5)
        flags = get_command_flags()
        if 'U' in flags: print("up")
        if 'D' in flags: print("down")
        if 'L' in flags: print("left")
        if 'R' in flags: print("right")
        if 'A' in flags: print("fire")
        if 'B' in flags: print("eject")

# END
