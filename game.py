# game.py  (c) 2017 D.J.Whale  22/01/2017
# Star-Wars 'Use the Force, Luke' game
# Using many moving parts provided by Martin O'Hanlon


#----- CONFIGURATION ----------------------------------------------------------

DEATHSTAR_CENTRE_POS = (100,100,10)
TARGET_POS           = (100,100,10)
IN_RANGE             = ((100,100,10), (100,100,10))
XWING_START_POS      = (10,10,10)
PLAY_TIME_SECS       = 5 #(2*60)
NUMBER_OF_TRIES      = 3
FRAMES_PER_SEC       = 10


#TODO: Mart's code animates the trench separately from deathstar
#so do we need to switch over to that animation at the right position?
#also is there a visual clue to where the trench is, in the deathstar model?

#TODO: xwing can turn or shift
#might make it turn if you tilt it left or right a long way
#in which case we need l,L and r,R for two ranges of left and right tilt


#----- LOAD ALL THE DEPENDENT PARTS -------------------------------------------

import sys
if sys.version_info[0] != 2:
    print("Please run this game with Python version 2")
    sys.exit()

import time
#TODO: import microbit      # auto-connects to micro:bit
#TODO: import starwars      # auto-connects to Minecraft
#TODO: import pygame       # for sounds

# LOAD SOUNDS
#TODO:   init pygame
#TODO:   init pygame mixer
#TODO:   load pygame sounds into buffers


#----- GAME STATE -------------------------------------------------------------

deathstar      = None
xwing          = None
missile        = None
xwing_crashed  = False
missile_missed = False
missile_hit    = False
game_stop_time = 0


#----- BUILD THE GAME WORLD ---------------------------------------------------

def clear_space():
    print("will clear_space")
    #TODO:

def build_deathstar():
    print("will build_deathstar")
    #TODO: build at DEATHSTAR_CENTRE_POS

def create_xwing():
    print("will build_xwing")
    #TODO: build at XWING_START_POS

def setup_game():
    clear_space()
    build_deathstar()
    create_xwing()
    clear_flags()

def wait_for_start():
    print("will wait_for_start")
    raw_input("press RETURN to start")
    #TODO: wait for A button press on micro:bit
    #loop, read from micro:bit, until see 'A'


#----- GAME ACTIONS -----------------------------------------------------------

def fly_xwing():
    print("will fly_xwing")
    #TODO:
    # read from micro:bit
    #   will be one of: ['U','D','L','R','A','B']
    # if U D L R (l?, r?)
    #   change xwing position
    # (always) move xwing forward by one block
    #
    # if xwing crashes into any block
    #   set_xwing_crashed()
    # elif A
    #   start_missile()
    # elif B # ejector seat
    #   ejector_seat()

def start_missile():
    print("will start_missile")
    #TODO:
    # create missile object in front of xwing
    # note we need to know what direction the xwing is flying in
    # we also need to know a range of positions to succeed from

def move_missile():
    print("will move_missile")
    #TODO:
    # if missile now out of range:
    #   set_missile_missed()
    # elif missile not yet hit target:
    #   move missile forward by 1
    # else must have hit
    #   set_missile_hit()

def ejector_seat():
    print("will ejector_seat")
    animate_eject()
    animate_xwing_crashed()
    set_xwing_crashed()


#------ GAME CONDITIONS -------------------------------------------------------
#
# Set various game conditions in the game state.
# The main loop will detect and action these appropriately.
# This prevents passing lots of variables around,
# but contains the global variables a bit more into a controlled space (here)

def clear_flags():
    global xwing_crashed, missile_missed, missile_hit
    xwing_crashed  = False
    missile_missed = False
    missile_hit    = False

def set_xwing_crashed():
    global xwing_crashed
    xwing_crashed = True

def set_missile_missed():
    global missile_missed
    missile_missed = True

def set_missile_hit():
    global missile_hit
    missile_hit = True


#----- ANIMATIONS -------------------------------------------------------------

def animate_missile_missed():
    print("will animate_missile_missed")
    #TODO:

def animate_missile_hit():
    print("will animate_missile_hit")
    #TODO:

def animate_eject():
    print("will animate_eject")
    #TODO:

def animate_xwing_crashed():
    print("will xwing_crashed")
    #TODO:

def animate_blow_up_deathstar():
    print("will blow_up_deathstar")
    #TODO:
    # auto pilot the ship to a safe location
    # animate the deathstar blowing up
    # return when deathstar gone


#----- SPLASH SCREENS ---------------------------------------------------------

def splash_screen():
    print("will splash_screen")
    #TODO:

def game_over_failed():
    print("will game_over_failed")
    #TODO:

def game_over_succeeded():
    print("will game_over_succeeded")
    #TODO:


#----- GAME LOOP --------------------------------------------------------------

def start_game():
    global game_stop_time
    print("will start_game")
    #TODO: move player to position on start (hides splash screen)
    game_stop_time = time.time() + PLAY_TIME_SECS

def run_out_of_time():
    return time.time() >= game_stop_time

def play_game():
    missiles_left = NUMBER_OF_TRIES

    while not run_out_of_time() and not xwing_crashed and not missile_hit and missiles_left > 0:

        time.sleep(1/float(FRAMES_PER_SEC))

        fly_xwing()
        if missile is not None:
            move_missile()

        if missile_missed:
            animate_missile_missed()
            missiles_left -= 1

        elif missile_hit:
            animate_missile_hit()
            animate_blow_up_deathstar()

    return missile_hit


#----- MAIN PROGRAM -----------------------------------------------------------

while True:
    setup_game()
    splash_screen()
    wait_for_start()
    start_game()

    success = play_game()

    if success:
        game_over_succeeded()
    else:
        game_over_failed()

# END




