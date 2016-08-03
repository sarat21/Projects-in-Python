
#secs	x	        y	        velocity
#0	75.55848254	400.5876	0.5556
#1	75.55848254	400.5876	0.926
#2	78.0508653	400.4024	1.8892
#3	78.96910162	401.1432	2.4
#...

## The locations (coordinates) of each GPS measured point is
## given in x and y (they were already converted from longitude/latitude ...)
## These GPS points were measured on March 17, 2008, starting at 09:45:34,
## the first column (secs) contains the time (in seconds) for each
## point after this time. The last column contains the velocity of the car
## at each location (in km/h)

# You could treat gps_data.csv as a simple text file or use the csv module's reader
# object (csv.reader()), for both see lecture24 and it's code.
# Or you can read in the xls file but you'll need to install the xlrd module first.
# I've put some examples of using teh xlrd module at the end of lecture 24

import csv  # for reading csv (comma separated value) files, part of standard lib
#import xlrd #  need to be installed if you want to use the xls file instead, see lecture 24 (http://pypi.python.org/pypi/xlrd )
  

####################### Function definition Part ###############################
"""
Problem 1

Import the data from a spreadsheet and convert to lists of floats

   Write a function import_data(<filename>), that reads time, location (x and y) 
   and velocity from the spreadsheet file in into four separate lists and returns
   them as a list of 4 lists. 
   Don't forget to remove the first entry of each column, as the first
   line (row) of the spreadsheet only contains the column names (header).   
   As we will use these list for plotting, they need to contain floats (numbers), 
   not strings!

[ 6 pts ]
"""

def import_data(spreadsheet_filename):
    ''' 
    Imports data from a spreadsheet file and returns a list containing each column (!)
    of the spreadsheet as floats, NOT including the header!

    Example - this table
    
    secs	x	        y	        velocity
    0	        75.55848254	400.5876	0.5556
    1	        75.55848254	400.5876	0.926
    2	        78.0508653	400.4024	1.8892
    3	        78.96910162	401.1432	2.4
    ...         ...             ...             ...
    222         73.45968478     396.328         0.1852
    
    would be returned as a list containing 4 lists of floats (one for each column), here:

    [ 
      [0, ..., 222], <- secs
      [75.55848254 , ..., 73.45968478],  <- x
      [400.5876, ..., 396.328],  <- y
      [0.5556, ..., 0.1852] <- vel
    ]
    
    '''
    
    
    # lists to hold each spreadsheet columns  
    t_secs = [] # time in seconds
    x = [] # 
    y = [] # 
    vel_km_h = [] # velocity in kilometers per hour
    
    infile = open(spreadsheet_filename,"rU")
    reader = csv.reader(infile)
    
    list_4 = [] #List for reading in the csv file
    
    for row in reader:
        list_4.append(row)
    
    del list_4[0] #Deleting the first row containing the header
    
    for i in range(0,len(list_4)):    #Creating 4 different lists: t_secs, x, y and vel_km_h from the list list_4
        t_secs.extend([float(list_4[i][0])])
        x.extend([float(list_4[i][1])])
        y.extend([float(list_4[i][2])])
        vel_km_h.extend([float(list_4[i][3])])
        
    return_list = [] # List of 4 lists
    return_list.append(t_secs)
    return_list.append(x)
    return_list.append(y)
    return_list.append(vel_km_h)
    
    
    return return_list # list of 4 lists of floats


############################ MAIN PART ######################################3        

  
filename = "GPS_data.csv"
#filename = "GPS_data_for_mac.csv"
#filename = "GPS_data.xls"

# import_data() will return a list of columns (lists)
cols = import_data(filename) # given a file name, function returns a list of column (as lists of numbers)

# give each column list a short name: t for 1. column, y for 2. column, etc.)
t,x,y,v = (cols[0], cols[1], cols[2], cols[3])


"""
Problem 2

Convert x,y and velocity from lists to numpy 1D arrays
   Optional: Use numpy to print out the type of numbers stored in each of the arrays
   Optional: Use numpy methods to print out the minimum , average, maximum and the standard deviation of the velocity array

[ 2 pts ] Create numpy arrays from lists fro x, y and v
[ +1 pt ] Print out the type of numbers stored in the array
[ +2 pts ] Print the average and standard deviation using numpy
"""
import numpy as np # all numpy names now start with np instead of numpy
x_ar = np.array(x)
y_ar = np.array(y)
v_ar = np.array(v)

print "Problem 2:"

#To print out type of numbers stored in the array:
print "Type of data in x_ar: ",x_ar.dtype
print "Type of data in y_ar: ",y_ar.dtype
print "Type of data in v_ar: ",v_ar.dtype

#To print out average and standard deviation:
print "For x_ar, Mean = ",np.mean(x_ar),"and Standard Deviation = ",np.std(x_ar)
print "For y_ar, Mean = ",np.mean(y_ar),"and Standard Deviation = ",np.std(y_ar)
print "For v_ar, Mean = ",np.mean(v_ar),"and Standard Deviation = ",np.std(v_ar)



"""
Problem 3

Graph the data in Matplotlib

[ 2 pt ]  Plot a red line through each GPS location
[ 1 pt ]  Add a grid
[ +1 pt ]  Make sure the grid is square (look up the argument for the axis() command!)
[ +1 pt ]  In addition to the line, add another plot where an x to marks each GPS location
"""

import matplotlib.pyplot as plt  # import pyplot style of matplotlib as plt

## plot a line through the GPS location points  
plt.figure()
plt.plot(x_ar,y_ar,color="red")
plt.title("Problem 3: Plot without markers")
plt.grid()
plt.axis("equal")
plt.show()
plt.savefig("Problem 3_Plot without markers.pdf")
plt.close()


## extra 1 pt: also plot x at each location
plt.figure()
plt.plot(x_ar,y_ar,color="red",marker='x')
plt.title("Problem 3: Plot with markers")

## add a grid
plt.grid()

## As this plot is a map, set the axis to "equal" so that 1 unit along x is
## is plotted with the same physical distance as 1 unit along y. After this, the dotted 
## grid should be shown as squares,
plt.axis("equal") #To make sure the grid is square

plt.show()
plt.savefig("Problem 3_Plot with markers.pdf")
plt.close()






"""
Problem 4

Add a title that shows the start and end time of the run

[ 2 pts ]
"""
import time
import datetime

# Let's assume you know that the trip started at 9 hours 45 minutes and 34 seconds on  March 17, 2011.
# Convert this information into a datetime object  
#start_time = datetime.datetime(???)
start_time = datetime.datetime(2011, 3, 17, 9, 45, 34)

# Pull out last entry in the time column (1. column) - set this as the length of the trip in seconds
len_time = len(t)
trip_length_element = len_time - 1
trip_length_in_seconds = t[trip_length_element]

# Creates a deltatime object from this time difference from the start of the tripnumber of seconds
tdiff = datetime.timedelta(seconds=int(trip_length_in_seconds))

# Now that have the start_time and the time difference (tdiff) to the end of the trip
# calculate the time (as in hours minutes seconds) it will be at the end of the trip 
# (i.e. after trip_length_in_seconds passed ...)
end_time = start_time + tdiff

# use the standard str() function to convert both of your datetime objects to strings. 
# Each string should look something like this: '2011-03-17 09:45:34'
start_time_str = str(start_time)
end_time_str = str(end_time)

# Using these time strings make a plot title like this "Start 09:45:34    End ??:??:??" 
title_str = "Start " + start_time_str + "  End " + end_time_str # make a full title
plt.plot(x_ar,y_ar,color="red")
plt.title(title_str)
plt.grid()
plt.axis("equal")
plt.show()
plt.savefig("track.pdf") #Saving the plot as a pdf file called "track.pdf"
plt.close()


"""
Problem 5

Show the plot on your screen. Either make a screenshot of the application (track.jpg)
    or use a matplotlib method to save the figure as a pdf file called track.pdf
    Should look similar to track_example.pdf
    

[ 1 pt ]
"""
#Done in the code for Problem 4 (Line 234 of code)


"""
Problem 6

Optional:  Indicate the x/y location on the plot where the car drove at top
    speed (had the highest velocity) with a text like this "<-79.2 km.h" (look at 
    the text() method and use align the text left). Round your top speed to one digit.
    
    In your code, explain how you found the x/y location of highest velocity 
    Take a screen shot.


[ +2 pts ]
"""
#To find highest velocity
max_vel = max(v)

#To find index of max_vel in the list v
max_vel_index = v.index(max_vel)

#To find corresponding x and y coordinates:
max_vel_x = x[max_vel_index]
max_vel_y = y[max_vel_index]

plt.figure()
title_str = "Start " + start_time_str + "  End " + end_time_str # make a full title
plt.plot(x_ar,y_ar,color="red")
plt.title(title_str)
plt.grid()
plt.axis("equal")

#Rounding top speed to one digit
new_vel_x10 = max_vel*10
new_vel = int(new_vel_x10)/10.0
new_vel_str = str(new_vel)
display_text = "<-" + new_vel_str + "km.h"
plt.text(max_vel_x,max_vel_y,display_text,horizontalalignment="left")
plt.show()
plt.savefig("Problem 6.pdf") #Saving the plot as a pdf file called "Problem 6.pdf"
plt.close()




