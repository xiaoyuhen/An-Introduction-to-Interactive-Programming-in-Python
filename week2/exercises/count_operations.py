# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

conut = 0

# Define event handlers for four buttons

def reset():
    global count
    count = 0
    
def increment():
    global count
    count += 1

def print_count():
    print count
    
def decrement():
    global count
    count -= 1
    

    
# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame('manipulate', 200, 200)
frame.add_button('reset', reset)
frame.add_button('inrement', increment)
frame.add_button('decrement', decrement)
frame.add_button('print count', print_count)

# Start the frame animation


frame.start()
    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()        
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2

