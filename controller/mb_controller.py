# mb_controller.py - a simple controller module using serial polling of a micro:bit

import microbit # will auto-connect to micro:bit

def get_command_flags():
    """Get a collection of flags, one for each possible button/action"""

    return microbit.read()


#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__": # test harness
    while True:
        flags = get_command_flags()
        if flags is not None:
            if 'U' in flags: print("up")
            if 'D' in flags: print("down")
            if 'L' in flags: print("left")
            if 'R' in flags: print("right")
            if 'A' in flags: print("fire")
            if 'B' in flags: print("eject")

# END
