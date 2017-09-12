# Image debugging problem

###################################################
# Student should enter code below

import simplegui

# load test image
test_image = simplegui.load_image("http://i.imgur.com/PIOFgal.jpg")
test_image_size = [test_image.get_width(), test_image.get_height()]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, [test_image_size[0], test_image_size[1]])

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw)


# start frame
frame.start()
        
                                       
