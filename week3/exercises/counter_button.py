# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    

def start_button_handler():
    timer.start()
    
def stop_button_handler():
    timer.stop()
    
def reset_button_handler():
    global counter
    counter = 0
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button('Start', start_button_handler)
frame.add_button('Stop', stop_button_handler)
frame.add_button('Reset', reset_button_handler)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

