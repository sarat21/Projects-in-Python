'''

'''
import math 
import turtle

"""
Problem 1

Mandatory: Complete the function check_input() and use it to check that the angle is between 0 and 90 (degrees)
You will need to finish the function definition before you can call it in the main loop!

[ 2 pts ] finish the check_input() function
"""
def check_input(input_to_check):
    ''' 
    Expects a number(!) in input_to_check
    returns True if input_to_check is between 0 and 90
    returns False otherwise
    '''
    # check if input_to_check is bigger 0 and assign the result (True/False) to a variable
    if input_to_check > 0 :
        result1 = True
    else:
        result1 = False
    
    # check if input_to_check is smaller than 90 and assign the result (True/False) to another variable    
    if input_to_check < 90 :
        result2 = True
    else:
        result2 = False
    

    # if both variables contain True, return True, in any other case return False
    if (result1 == True) and (result2 == True):
        return True
    else:
        return False

    # Note: there are many shorter solutions to this, which you are welcome to use (it can be done in a single line).
    
#The shorter solution to this is :-

#def check_input(input_to_check):
    #if (input_to_check>0) and (input_to_check<90):
        #return True
    #else:
        #return False

    
    
   



"""
Problem 2

Draw the trajectory (function)
    
Mandatory: Nothing to do, I've given you the basic version of the draw_trajectory() function, 
           use it to draw the flight of the turtle. 

Optional: you get extra points to if you improve the function buy adding code to:

a) visualize the y-velocity during flight via the line "thickness" i.e. the size of the pen. 
The lowest velocity (around 0, at the apex) should be drawn with a size of 1.0, 
the highest possible velocity, always the initial velocity (30 by default) with a size of 5.0. 
Note that velocity is a signed number, it will be negative from the apex downwards. Your thinkness should be based 
on the absolute y-velocity, you can use the abs() or math.fabs() function.

b) adjust the turtle's tilt angle during the actual flight so it points along 
the trajectory (note: this is pretty tricky to do!). Use settiltangle(). To get the current angle you'll
you you will have to keep track of the LAST x/y position and subtract it from the current x/y position.
Look up the math.atan2() function to get an angle from this difference (vector).

[ +2 pts ] Optional 
[ +4 pts ] Optional 
"""
def draw_trajectory(initial_velocity, launch_angle_degrees, target_start, target_end):
    '''
    Function that draws the turtle trajectory, returns true if target was hit
    
    Arguments (all are numbers):
      initial_velocity - initial velocity at a lauch angle  of launch_angle_degrees
      target_start, target_end - distances to the target (target_end - target_start is the width of the target)
      
    Returns: 
      True if the ball hits the ground between target_start and target_end meters away from the cannon 
      False if target was missed
    
    Note:
      Will print out a table for the position and speed of the turtle for each time step
    '''

    # starting turtle coordinates (i.e. the location of the cannon)
    x_pos = 0.0
    y_pos = 0.0 
    t.penup()
    t.hideturtle()
    t.goto(x_pos, y_pos) # move to lower left corner of canvas
    t.pendown()
    t.showturtle()

    # starting velocity in x and y
    launch_angle_radians = math.radians(launch_angle_degrees)
    y_vel_initial = initial_velocity * math.sin(launch_angle_radians)
    x_vel_initial = initial_velocity * math.cos(launch_angle_radians)
    y_vel = y_vel_initial
    x_vel = x_vel_initial

    time = 0.0 # current time, starting a 0.0 seconds
    time_increment = 0.1  # time increment for each simulation step in seconds

    print "time\tx-pos\ty-pos\tx-vel\ty-vel" # header for printing the flight data table

    while y_pos > -0.000001:  # loop while y_pos is above ground (y_pos > 0.0 didn't work for me ...)
        
        # Store the last x/y position before new position is calcualted
        last_x = x_pos
        last_y = y_pos   
            
        # for the current time, calculate velocity and distance in x and y
        y_vel = y_vel_initial - GRAVITY * time #        
        x_vel = x_vel # no change over time
        x_pos = x_vel * time  # x coordinate of ball at current time
        y_pos = y_vel_initial * time - 0.5 * GRAVITY * time * time
        
        
        # Optional: add code to a) visualize the y-velocity and b) tilt the turtle during flight
        '''
        vel_fraction = y_vel/float(initial_velocity)
        pen_size_fraction = vel_fraction * 4
        new_pen_size = 1 + pen_size_fraction
        t.pen(pensize=new_pen_size)
        
        I tried to add this code but even though this worked for smaller angles, it did not seem to work for larger angles because of something it called "bad screen distance" and thus gave me an error for larger angles.
        '''
        
        t.goto(x_pos, y_pos)  # move the turtle to the current position     

        # print out flight data 
        print  time, "\t", round(x_pos,1), "\t", round(y_pos,1), "\t", round(x_vel,1), "\t", round(y_vel,1)
        time = time + time_increment    
    # end of while loop

    # we left the while loop, so the ball must have hit the ground!
    # (actually, it's slightly below the ground, so let's reposition the turtle to just above the ground..
    t.penup()   # pen up (so we don't leave a trace when moving it up)
    t.sety(0.1) # go up to 0.1 above "ground level"  

    # We hit the ground - but did we hit the target? (check x-coordinate)
    if x_pos > target_start and x_pos < target_end:
        return True
    else:
        return False


"""
Problem 3

Mandatory: Nothing to do, position and size of target are hardcoded
Optional: Randomly place the target (keep it 10 wide), so that its center is somewhere between 50 and 90
[ +1 pt ] Optional 
"""
# size of convas, 1 pixel corresponds to 1 meter in reality
max_x = 100 # width
max_y = 100  # height


## target placement (must be between 0 and max_x!)
#target_x_start = 80
#target_x_end = 90
##^Commented out since optional part is implemented 

# Optional: instead of hard coding it, put it randomly between 50 and 90 (10 wide)
import random
target_x_start = random.randint(50,85) #Range is limited to 85 so that the center of the target does not exceed 90.
target_x_end = target_x_start + 10



# -------------------------------- MAIN part -----------------------------------

# prep the canvas, draw and draw the ground as brown line and target in red
t = turtle
t.setworldcoordinates(0,-0,max_x, max_y) # set canvas (meters)

# draw a line at y=0.0 to serve as ground  
t.speed(0) # so ground line drawing happens instantly
t.penup()
t.goto(0,0) # draw ground
t.pendown()
t.pencolor("brown")
t.goto(max_x,0)

# draw a red target at y=0 from x=target_x_start to x=target_x_stop
t.penup()
t.goto(target_x_start,0)
t.pendown()
t.pencolor("red")
t.pensize(10)  # draw fat line 
t.goto(target_x_end,0)
t.penup()

# prepare for drawing the trajectory as black line
t.pencolor("black")
t.pensize(1)
t.goto(0,0)
t.speed("slow")
t.shape("turtle") # flying turtle

GRAVITY = 9.81 # g at m/s2 on Earth 
number_of_shots = 1 # number of shots fired in current game
target_was_hit = False # Flag, will be True when target was hit
initial_velocity = 30.0  # default m/s velocity at which the turtle leaves the cannon 

print "Trajectory game - try and hit the target with the turtle"
print "Velocity is", initial_velocity 




"""
Problem 4

This is the main loop, it's already designed to end when the target was hit.

Mandatory: Inside the loop, use your check_input() function to verify that the user entered 
an angle between 0 and 90.  
[ 2 pts ] use check_input() to verify input

Optional: You'll get extra points for adding code for the following enhancements:
a) If the user enters "quit" instead of an angle, exit the while loop and quit the game
b) Keep track of how many shots were needed to hit the target.
   if the target was NOT hit print out "you missed with shot X" (X: 1,2,3,4,...) 
   it the target as hit print out "You won with X shots"
[ +1 pts ] Optional   
[ +1 pts ] Optional   
"""

try_count=0 # initializing number of tries to 0.
    # draw the trajectory, returns True when target was hit
    
while target_was_hit == False:   # As long as the target was not hit, repeat the following ... 

    # Get user input as a string
    angle_str = raw_input("Enter the cannon angle (0-90 degrees) ") # string with angle of cannon, 0 is horizontal, 90 is upwards
    
    # Optional: let user quit by typing in 'quit'
    if angle_str == "quit":
        break
    
    
    angle = float(angle_str) # convert string to a float number
        
    # use check_input() to verify that the user entered a number between 0 and 90
    # if the check fails, jump back to: while target_was_hit == False:  
    if check_input(angle) is True:
        print "Angle is between 0 and 90"
    else:
        print "Angle entered is not between 0 and 90. Enter cannon angle again."
        continue
    
    
    target_was_hit = draw_trajectory(initial_velocity, angle, target_x_start, target_x_end)
    if not target_was_hit:
        try_count += 1
        print "You missed with shot ",try_count    #Prints the try number  
    else:
        try_count += 1
        print "You won with",try_count,"shots!"     #Prints the total number of tries after which the target was hit
     
         
# game loop ends here - user did hit target
print "Game over"

raw_input("Waiting for you to press any key") # wait so you can make a screenshot
turtle.bye() # clean up

