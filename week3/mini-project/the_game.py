# template for "Stopwatch: The Game"

import simplegui

# define global variables

total_ticks = 0
total_count = 0
right_count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    mins = t / 100 / 60
    seds = t / 100.0 % 60
    text = str(mins) + ':' + str(seds)
    return text
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button_handler():
    global total_count
    total_count += 1
    timer.start()
    
def stop_button_handler():
    global right_count
    if total_ticks % 500 == 0:
        right_count += 1
    timer.stop()
    
def reset_button_handler():
    global total_ticks, total_count, right_count
    total_ticks = 0
    total_count = 0
    right_count = 0
    

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global total_ticks
    total_ticks += 10

# define draw handler

def draw_handler(canvas):
    text = format(total_ticks)
    count = str(right_count) + '/' + str(total_count)
    canvas.draw_text(count, [160, 20], 20, 'Green')
    canvas.draw_text(text, [70, 110], 40, 'White')
    
# create frame

frame = simplegui.create_frame('the game', 200, 200)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers

frame.add_button('Start', start_button_handler)
frame.add_button('Stop', stop_button_handler)
frame.add_button('Reset', reset_button_handler)

# start frame

frame.start()


# Please remember to review the grading rubric

