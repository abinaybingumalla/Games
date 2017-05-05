# implementation of card game - Memory

import simplegui
import random

sublist = [0,1,2,3,4,5,6,7]
list1 = sublist + sublist
random.shuffle(list1) 
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
index = [ [0,50],[50,100],[100,150],[150,200],[200,250],[250,300],[300,350],[350,400],[400,450],[450,500],[500,550],[550,600],[600,650],[650,700],[700,750],[750,800]]
idx1 = 0
idx2 = 0
state = 0
turns = 0

# helper function to initialize globals
def new_game():
    global list1,exposed,idx1,idx2,turns,state
    random.shuffle(list1) 
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    idx1 =0
    idx2 = 0
    turns = 0
    state = 0
    label.set_text("Turns = " + str(turns)) 

     
# define event handlers
def mouseclick(pos):
    for i in range(0,16):
        if index[i][0] < pos[0] and pos[0] < index[i][1]: 
            if not exposed[i]:    
                global state , idx1 ,idx2 ,turns
                if state == 0:                    
                    state = 1
                    exposed[i] = True
                    idx1 = i
                   
                elif state == 1:
                    state = 2
                    exposed[i] = True 
                    idx2 = i                    
                    turns += 1
                    label.set_text("Turns = " + str(turns)) 
                else:
                    state = 1 
                    if list1[idx1] != list1[idx2]:
                        exposed[idx1] = False
                        exposed [idx2] = False
                    exposed[i] = True
                    idx1 = i
                  
    #cards are logically 50x100 pixels in size    
def draw(canvas):
    a = 20 
    b = 0
    
    for i in range(0,len(list1)):
        if not exposed[i] :
            b = i*50
            canvas.draw_polygon([(b, 0), (b+50, 0),(b+50,100),(b, 100)], 2, 'Black','Green')
        else:
            a = i*50
            canvas.draw_text(str(list1[i]),(a+20, 60), 30, 'White')
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()