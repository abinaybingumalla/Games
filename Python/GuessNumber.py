# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global original , count , s3
    s3 = ""
    range100()
     
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global original , count ,s1 ,s2,s3
    count = 7
    original = random.randrange(0,100)
    s1 = "New Game. Range is from 0 to 100"
    s2 = "No of remaining guesses is " + str(count)
    s3 = ""
    return original
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global original , count , s1 , s2 ,s3
    count = 10
    s1 = "New Game. Range is from 0 to 1000"
    s2 = "No of remaining guesses is " + str(count)
    s3 = ""
    original = random.randrange(0,1000)
    return original
    
   
    
def input_guess(guess):
    # main game logic goes here	
    global original,count , s2 , s3 , s1
    s1 = "Guess was "+ str(int(guess))
    
    if(count !=0):
        if(int(guess) > original):
            count = count-1
            s2 = "No of remaining guesses is " + str(count)
            s3 = "Lower!"  
            

        if(int(guess)< original):
            count = count-1
            s2 = "No of remaining guesses is " + str(count)
            s3 = "Higher!"  
            
        if(int(guess)== original):
            count = count-1
            s1 = ""
            s2 = "Your Guess is Correct"  
            s3 = " Play Again ! "
            
    else:
        s2 = "You Lost !!"
        s3 = "Try Again"
        s1 = "Actual Number was " + str(original)
        

def draw(canvas):
    global s1 , s2 , s3
    canvas.draw_text(s1,[100,140],24,"white")
    canvas.draw_text(s2,[100,175],24,"white")
    canvas.draw_text(s3,[100,210],24,"white")
    
# create frame
f = simplegui.create_frame("GUESS NUMBER",600,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0 to 100]",range100,200)
f.add_button("Range is [0 to 1000]",range1000,200)
f.add_input("Enter the guess",input_guess,200)
f.start()
f.set_draw_handler(draw)

# call new_game 
new_game()


