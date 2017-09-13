# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global exposed_dict, exposed_idx_dict, exposed_num_dict, count, exposed, turns
    count = 0
    turns= 0
    exposed = []
    exposed_dict = {}
    total_list = []
    exposed_idx_dict = []
    exposed_num_dict = []
    total_object = {}
    a_list = range(8)
    b_list = range(8)
    exposed.extend(a_list)
    exposed.extend(b_list)
    random.shuffle(exposed)
    Turns = 'Turns = ' + str(turns)
    label.set_text(Turns)
    
    for idx, i in enumerate(exposed):
        exposed_dict[idx] = {i : False}

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, exposed_dict, count, exposed_num_dict, exposed_idx_dict, turns, Turns
    num = pos[0] // 50
    if not exposed_dict[num][exposed[num]]:
        if count < 2:
            exposed_dict[num][exposed[num]] = True
            exposed_num_dict.append(num)
            exposed_idx_dict.extend([exposed[num]])
            count += 1
        else:
            if exposed_idx_dict[0] == exposed_idx_dict[1]:
                exposed_dict[num][exposed[num]] = True
            else:
                exposed_dict[exposed_num_dict[0]][exposed_idx_dict[0]] = False
                exposed_dict[exposed_num_dict[1]][exposed_idx_dict[1]] = False
                exposed_dict[num][exposed[num]] = True
            count = 1
            turns += 1
            Turns = 'Turns = ' + str(turns)
            label.set_text(Turns)
            exposed_num_dict = [num]
            exposed_idx_dict = [exposed[num]]
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx, i in enumerate(exposed_dict):
        for idx2, j in enumerate(exposed_dict[i]):
            if exposed_dict[i][j]:
                canvas.draw_text(str(j), [15 + idx * 50, 60], 40, 'White')
            else:
                polygon_top_left = [0 + idx * 50, 0]
                polygon_top_right = [50 + idx * 50, 0]
                polygon_bottom_left = [0 + idx * 50, 100]
                polygon_bottom_right = [50 + idx * 50, 100]
                canvas.draw_polygon([polygon_top_left, polygon_top_right, polygon_bottom_right, polygon_bottom_left], 1, 'Black', 'Blue')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

