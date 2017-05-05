# template for "Stopwatch: The Game"

import simplegui

# define global variables
min = 0
sec = "00"
milli = 0
t = 0
text = "0:00.0"
score = 0
actual = 0
final = str(score)+ "/" + str(actual)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global min,sec,milli,text
    milli = t % 10
    min = ((t - milli)/10)/60
    sec = (t - milli-(min*600))/10
    if sec <10 :
        text = str(min) + ":0" + str(sec)+ "." + str(milli)
    else :
        text = str(min) + ":" + str(sec)+ "." + str(milli)
        
    return t
   
def update():
    global final,actual,score
    final = str(score)+ "/" + str(actual)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start(): 
    timer.start()
    

def stop():    
    global actual , score , t , actual 
    
    actual = actual + 1
    
    if (t%50) == 0 :
        score = score +1 
    update()
    timer.stop() 
    
def reset():
    global t , score ,actual
    t = 0
    score = 0
    actual = 0
    update()
    format(t)
    timer.stop()
    
        
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t + 1
    format(t)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(text,[125,110],24,"white")
    canvas.draw_text(final,[265,20],24,"white")
    
# create frame
frame = simplegui.create_frame("STOP WATCH",300,200)

# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)

# start frame
frame.start()


