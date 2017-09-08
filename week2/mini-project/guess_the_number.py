# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

count = 0
range_type = '100'

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    range100()
    print secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, range_type
    range_type = '100'
    secret_number = random.randrange(0, 100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global secret_number, range_type
    range_type = '1000'
    secret_number = random.randrange(0, 1000)
    
def input_guess(guess):
    # main game logic goes here
    user_guess = int(guess)
    if range_type == '100' and (user_guess > 100 or user_guess < 0):
        print "please input 0-100 number"
    elif range_type == '1000' and (user_guess > 1000 or user_guess < 0):
        print "please input 0-1000 number"
    else:
        print 'Guess was ' + guess
        global count
        if (range_type == '100' and count > 7) or (range_type == '1000' and count > 10):
            print 'you have no chance'
        else:
            count += 1
            if user_guess > secret_number:
                print 'Higher'
            elif user_guess < secret_number:
                print 'Lower'
            else:
                print 'you win!'
                new_game()

    
# create frame

frame =simplegui.create_frame('input_frame', 200, 200)
frame.add_button('range100', range100)
frame.add_button('range1000', range1000)
frame.add_input('input_guess', input_guess, 100)

# register event handlers for control elements and start frame

frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

