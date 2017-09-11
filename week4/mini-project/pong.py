# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
win = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, win # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if score1 > 4 or score2 > 4:
        win = True
    else:
        if direction:
            ball_vel = [2, random.choice([2, -2])]
        else:
            ball_vel = [-2, random.choice([2, -2])]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = [HEIGHT / 2 - HALF_PAD_HEIGHT - paddle1_vel, HEIGHT / 2 + HALF_PAD_HEIGHT]
    paddle2_pos = [HEIGHT / 2 - HALF_PAD_HEIGHT, HEIGHT / 2 + HALF_PAD_HEIGHT]
    
    spawn_ball(random.choice([LEFT, RIGHT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), [150, 100], 40, 'White')
    canvas.draw_text(str(score2), [400, 100], 40, 'White')
    if win:
        if score1 > score2:
            win_text = 'left player win!'
        else:
            win_text = 'right player win!'
        ball_vel = [0, 0]
        canvas.draw_text(win_text, [50, 300], 80, 'Red')
        
        
    # update ball
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += -ball_vel[1]

            
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 20, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0] -= paddle1_vel
    paddle1_pos[1] -= paddle1_vel
    paddle2_pos[0] -= paddle2_vel
    paddle2_pos[1] -= paddle2_vel
    
    # draw paddles
    
    canvas.draw_line([0, paddle1_pos[0]], [0, paddle1_pos[1]], PAD_WIDTH * 2, 'White')
    canvas.draw_line([WIDTH, paddle2_pos[0]], [WIDTH, paddle2_pos[1]], PAD_WIDTH * 2, 'White')
    
    # determine whether paddle and ball collide
    x_collide = ball_pos[1] < (BALL_RADIUS + PAD_WIDTH)  or ball_pos[1] > (HEIGHT - BALL_RADIUS - PAD_WIDTH)
    y_collide = ball_pos[0] < (BALL_RADIUS + PAD_WIDTH * 2) or ball_pos[0] > (WIDTH - BALL_RADIUS - PAD_WIDTH * 2)
    is_left_paddled = ball_pos[1] > paddle1_pos[0] and ball_pos[1] < paddle1_pos[1]
    is_right_paddled = ball_pos[1] > paddle2_pos[0] and ball_pos[1] < paddle2_pos[1]
    if x_collide:
        ball_vel[1] = -ball_vel[1]
    elif y_collide and (is_left_paddled or is_right_paddled):
        ball_vel[0] = -ball_vel[0] * 1.3
        ball_vel[1] = ball_vel[1] * 1.3
    
    # draw scores
    
    is_right_score = ball_pos[0] + 2 <= (BALL_RADIUS + PAD_WIDTH * 2)
    is_left_score = ball_pos[0] - 4 >= (WIDTH - BALL_RADIUS - PAD_WIDTH * 2)
    if is_left_score:
        score1 += 1
        spawn_ball(random.choice([LEFT, RIGHT]))
    elif is_right_score:
        score2 += 1
        spawn_ball(random.choice([LEFT, RIGHT]))
        
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = paddle1_vel + 5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = paddle1_vel - 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = paddle2_vel + 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = paddle2_vel -5


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()


