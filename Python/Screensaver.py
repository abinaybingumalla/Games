import simplegui
import random

#global variables
message = "Enter your Name!"
width = 500
height = 500
position = [100,100]
interval = 1000


#define handlers
def draw(canvas):
    canvas.draw_text(message,position,28,"white")
def tick():
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    position[0] = x
    position[1] = y
def update(text):
    global message
    message = text
    
#Create frame
f = simplegui.create_frame("message",width,height)

#register Handlers
f.set_draw_handler(draw)
t = simplegui.create_timer(interval,tick)
text = f.add_input("Message : ",update,100)

#start frame
f.start()
t.start()