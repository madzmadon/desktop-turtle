########################## FINAL PROJECT #############################################
# GROUP MEMBERS:
    #Madison Evans
    # Adrianna Barrera
    # Kathryn Kaelin
# TOPIC:
    # Desktop Pet Turtle
######################################################################################


# Import necessary modules 
import random 
import tkinter as tk

# Print current working directory path
from pathlib import Path
print(Path.cwd())

SCREEN_WIDTH = 1440 # Set width of program screen area 
SCREEN_HEIGHT = 900 # Set height of program screen area

x = 100 # Starting x position for turtle
y= 100 # Starting y position for turtle

cycle = 0 # Animation cycle counter
check = 1 # Used to track current animation event
idle_num =[1,2,3,4] # Event numbers that trigger idle animation
sleep_num = [10,11,12,13,15] # Event numbers that trigger sleep animation
walk_left = [6,7] # Event numbers to walk left
walk_right = [8,9] # Event numbers to walk right  

event_number = random.randrange(1,3,1) # Pick a starting event  

# Path to folder containing gif images
impath = '/Users/madisonevans/Desktop/desktop-turtle/'
#'/Users/madisonevans/Desktop/desktop-turtle/'
#'/Users/kathr/OneDrive/Desktop/Multimedia/FinalProject/desktop-turtle/'

# Logic to keep x,y positions within screen boundaries
def clamp(val, min, max):
  return min if val < min else max if val > max else val


# Main event handling logic 
def event(cycle,check,event_number,x,y):
    
    if event_number in idle_num:  # If idle event  
        check = 0 # Update event tracker  
        print('idle') # Debug print  
        window.after(400,update,cycle,check,event_number,x,y) # Schedule next update, idle speed  

    elif event_number == 5: # If idle->sleep event 
        check = 1
        print('from idle to sleep')
        window.after(100,update,cycle,check,event_number,x,y) #no. 5 = idle to sleep
        
    elif event_number in walk_left: # Handle walk left
        check = 4
        print('walking towards left')
        window.after(400,update,cycle,check,event_number,x,y)#no. 6,7 = walk towards left
    
    elif event_number in walk_right: # Handle walk right
        check = 5
        print('walking towards right')
        window.after(400,update,cycle,check,event_number,x,y)#no 8,9 = walk towards right
   
    elif event_number in sleep_num: # Handle sleep
        check  = 2
        print('sleep')
        window.after(600,update,cycle,check,event_number,x,y)#no. 10,11,12,13,15 = sleep
   
    elif event_number == 14: # Handle sleep->idle events  
        check = 3
        print('from sleep to idle')
        window.after(100,update,cycle,check,event_number,x,y)#no. 15 = sleep to idle

# Logic to cycle through gif frame animation
def gif_work(cycle,frames,event_number,first_num,last_num):
    
    if cycle < len(frames) -1: # Haven't reached last frame
        cycle+=1
    else:
        cycle = 0 # Reset cycle count
        event_number = random.randrange(first_num,last_num+1,1) # Pick new event
    return cycle,event_number # Return updated animation & event variables

def update(cycle,check,event_number,x,y):
    #idle
    if check ==0:  # If idle event
        frame = idle[cycle] # Set current animation, call gif_work to cycle frames
        cycle ,event_number = gif_work(cycle,idle,event_number,1,9) # Update cycle counter and event_number
    #idle to sleep
    elif check ==1:
        frame = idle_to_sleep[cycle]
        cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,10,10)
    #sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle ,event_number = gif_work(cycle,sleep,event_number,10,15)
    #sleep to idle
    elif check ==3:
        frame = sleep_to_idle[cycle]
        cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1)
    #walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
        x += 1
        y += 1
    #walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
        x += -1
        y += -1
    
    # Keep x,y bounded by screen size using clamp()
    x = clamp(x, 0, SCREEN_WIDTH - 100)
    y = clamp(y, 0, SCREEN_HEIGHT - 100)
    window.geometry(f"115x65+{x}+{y}")
    
    # Resize gif for display & configure label
    frame = frame.zoom(3)
    frame = frame.subsample(15)
    
    label.configure(image=frame)
    label.image = frame
    

    window.after(1,event,cycle,check,event_number,x,y)
    
window = tk.Tk() # Create main app window 

############################## CALL BUDDYS ACTION GIF #####################################################
# Create list of PhotoImage objects for idle animation
# Iterate through images in a specific gif
#idle gif
idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
#idle to sleep gif
idle_to_sleep = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]
#sleep gif
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]
#sleep to idle gif
sleep_to_idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]
#walk to left gif
walk_positive = [tk.PhotoImage(file=impath+'walk-right.gif',format = 'gif -index %i' %(i)) for i in range(8)]
#walk to right gif
walk_negative = [tk.PhotoImage(file=impath+'walk-left.gif',format = 'gif -index %i' %(i)) for i in range(8)]

############################## WINDOW CONFIGURATION #####################################################

window.config(highlightbackground='black') # Make window transparent

# Additional settings to enable transparency effect
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparent', 'black')

label.pack()# Pack label to apply configs

############################## MAIN LOOP #####################################################

window.after(1,update,cycle,check,event_number,x,y) # Update animation frame, position etc. 
window.mainloop() # Start main loop

