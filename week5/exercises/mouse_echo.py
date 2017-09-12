# Echo mouse click in console

###################################################
# Student should enter code below

import simplegui

def mouseclick_handler(position):
    print 'Mouse click at (' + str(position[0]) + ', ' + str(position[1]) + ')'

frame = simplegui.create_frame('mouse click', 400, 400)
frame.set_mouseclick_handler(mouseclick_handler)

frame.start()


###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)
