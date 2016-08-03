
import turtle # needed for draw()
turtle.up()
import math

# Point class definition
class Point:  
    def __init__(self, x_coord=0, y_coord=0): #default args 
        # attributes: x and y coordinates
        self.x = x_coord
        self.y = y_coord 
        #print "instantiating an object",id(self), "of class", self.__class__.__name__, "with", self.x, self.y
    
    # Access methods    
    def set_x(self, new_x): 
        self.x = new_x
    def get_xy(self): 
        return (self.x, self.y) # return x/y pair in a tuple

    
    
    """
Problem 1

    Add four more additional access methods: set_y(), set_xy(), get_x, and get_y() methods.
    [ 4 pts ] add access methods
    """     
    def set_y(self,new_y):
        self.y = new_y
    
    def set_xy(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y 
    
  
    # Overloading:

    # overloading the addition (+) operator  
    def __add__(self, other_point): 
        added_x = self.x + other_point.x
        added_y = self.y + other_point.y 
        added_pt = Point(added_x, added_y)
        return added_pt # return new, "added" up instance
    

    """
Problem 2

    Overload the subtraction operator so that - can be used to subract points
    [ 2 pts ] overload the subtraction operator __sub__()
    """
    def __sub__(self, other_point):
        sub_x = self.x - other_point.x
        sub_y = self.y - other_point.y
        sub_pt = Point(sub_x, sub_y)
        return sub_pt #Returning the new, subtracted instance
  
    
  
    

    """
Problem 3

    Optional: Overload the equal (==) operator (__eq__()) so that  p2 == p1 returns  
    True if p2.x == p1.x and p2.y == p2.y, False otherwise. Test this in your main program 
    [ +1 pt ] overload equal (==) for shallow equality test 
    """
    
    def __eq__(self, p2):
        if (p2.x == self.x) and (p2.y == self.y):
            return True
        else:
            return False
    
    

    """ 
Problem 4

    Optional: add a dist() method that returns the 2D distance to a given point
    e.g. p1.dist(p2) -> 45.6    
    [ +1 pt ] impoment a dist() method
    """
    def dist(self,p2):
        x_diff = self.x - p2.x
        y_diff = self.y - p2.y
        d = math.sqrt((x_diff*x_diff)+(y_diff*y_diff)) #linear 2D distance between two points
        return d
    
    
    

   # overloading the str() method - creates a string representation, called when printing 
    def __str__(self):  
        my_attribs_and_values = "" # local string var, no self!
        for key, value in sorted(self.__dict__.items()): # loop through dict
            if not key[0] == "_": # if name does not start with _
                my_attribs_and_values += str(key) + ":" + str(value) + " " 
        return my_attribs_and_values # return assembled string for printing

    # draw() method - make turtle move to the point's location, draw a dot
    def draw(self): 
        turtle.goto(self.x, self.y)
        turtle.dot()

#------------------------------------------------------------------------------
 
# Polygon class - a sequence of Point objects
class Polygon: 
    def __init__(self, points=[]): # init with list of points
        print "creating an instance of class", self.__class__.__name__
        self.point_list = points[:]  # store a sequence of points
        
    def draw(self):
        turtle.penup()
        for p in self.point_list: 
            p.draw()
            turtle.pendown()
        # go back to first point to close the polygon
        self.point_list[0].draw()  
        
    def num_points(self):
        return len(point_list)
    
    
    
    

    """
Problem 5

    Optional: provide a length() method for the Polygon class that returns the 
    length of the polygon's outline by summing up the distances from each point to 
    the next, including the distance from the last point back to first point.
    For example for a 3 point polygon poly = Poly(p1, p2, p3), poly.length()
    should return distance from p1 to p2 plus the distance from  p2 to p3 plus the
    distance from p3 to p1. Test this in your main program on a polygon.
     
    [ +3 pt ] implement Polygon's length() method    
    """
    
#------------------------------------------------------------------------------
    

""" 
Problem 6

Define a Rectangle class, as another subclass (a specialization) of the Polygon class. 
Its __init__() arguments need to be the rectangle's lower left corner point, 
the rectangle's width  and rectangle's height. 

lowerleft = Point(5,5)
rt = Rectangle(lowerleft, 10, 15)

In the main program instantiate a rectangle with the lower-left corner 
at x=20, y=50 that's 80 (wide) by 150 (height)

Important: do NOT define an explicit draw() method for the Rectangle class.

[ +4 pt ] Rectangle class   
"""

class Rectangle(Polygon): 
    def __init__(self, lower_left_corner=Point(5,5), r_width=10, r_height=15):
        ll = lower_left_corner
        plst = [ll,                                  # lower-left
                ll+Point(r_width, 0),                # lower-right
                ll+Point(r_width,r_height),          # upper-right
                ll+Point(0, r_height)]               # upper-left
        Polygon.__init__(self, plst)






   
#------------------------------------------------------------------------------

# Square: a subclass (child) of the Polygon class 
class Square(Polygon): 
    def __init__(self, lower_left_corner=Point(0,0), side_length = 0):
        ll = lower_left_corner
        plst = [ll,                                  # lower-left
                ll+Point(side_length, 0),            # lower-right
                ll+Point(side_length, side_length),  # upper-right
                ll+Point(0, side_length)]            # upper-left
        Polygon.__init__(self, plst) # now go and make a polygon from that  
    # Although we do NOT define a draw() method for the Square class,
    # it already has the ability to draw itself (why?)



"""




