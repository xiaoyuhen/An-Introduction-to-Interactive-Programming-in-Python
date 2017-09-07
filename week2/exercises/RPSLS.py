# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return False
    
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return False

# Handler for input field
def get_guess(guess):
    print 'player choice ' + guess
    player_number = name_to_number(guess)
 
    computer_number = random.randrange(0, 4)
    computer_choice = number_to_name(computer_number)
    print 'Computer chooses ' + computer_choice
    
    if player_number and computer_number:
        if player_number == computer_number:
            print "Player and computer tie"
        elif player_number > computer_number:
            if player_number - computer_number == 1 or player_number - computer_number == 3:
                print "Player wins!"
            else:
                print "Computer wins!"
        else:
            print computer_number, player_number
            if computer_number - player_number == 1 or computer_number - player_number == 3:
                print "Computer wins!"
            else:
                print "Player wins!"
    else:
        print "Error: Bad input "+ guess + " to rpsls"
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#

