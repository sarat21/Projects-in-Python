"""
Problem 1

HCI 574 2015 midterm

Ex 1:  Index and slicing

Using both indexing and slicing, only on L, assemble and print a new list that 
looks like this:
[0, 2, 3, [5 ,6], 8, 10]

[ 3 pts ]
"""

L = [0, [], [1,2,3,4], [[5],[6,7]], [8,9,10]]
newL=[]

newL= [L[0],L[2][1],L[2][2],[L[3][0][0],L[3][1][0]],L[4][0],L[4][2]]
# newL = ...
#print "newL is", newL # should show this: [0, 2, 3, [5 ,6], 8, 10]




"""
Problem 2

Ex 2: For and while loops 

Write code, (using for and/or while loops) to figure out how often each element of F occurs within N and print it out.

This should print:
4 occurs in N 2 times
7 occurs in N 1 times
2 occurs in N 3 times

IMPORTANT: if use the count() function you will only get half points (because that's just too easy ...)
[ 6 pts ]
"""

F = [4,7,2]
N = [2,3,4,2,5,6,3,2,6,7,3,4]
count=0
for i in F:
 for a in N:
   if(i==a):
    count+=1
 print i,' occurs in N ',count,' times\n'
 count=0
 



 
  

"""
Problem 3

Ex 3: Function design

Write a function lenumerate() that takes a string (like s) and returns a list of 2-item lists
containing each word and it's length:
[['But', 3], ['then', 4], ['of', 2], ... ['are', 3], ['nonmigratory', 12]]

"""
def lenumerate(s):
 new=[]
 l=''
 for i in s:
  if(i!=' '):
   l=l+i
  else:
   new=new+[[l,len(l)]]
   l=''
 if(i!=' '):
  new=new+[[l,len(l)]]
 
 print 'Output: ',new

lenumerate(raw_input('Enter your string: '))

[ 3 pts ]
"""
Part 2 with FLip
"""
def lenumerate2(s,flip=None):
 if ((flip==None)or(flip==False)):
  new=[]
  l=''
  for i in s:
   if(i!=' '):
    l=l+i
   else:
    new=new+[[l,len(l)]]
    l=''
  if(i!=' '):
   new=new+[[l,len(l)]]
 else:
   new=[]
   l=''
   for i in s:
    if(i!=' '):
     l=l+i
    else:
     new=new+[[len(l),l]]
     l=''
   if(i!=' '):
    new=new+[[len(l),l]]  
   
 
 print 'Output: ',new
 
 """
 OUTPUT:
  lenumerate2('emilty jkg',True)
  Output:  [[6, 'emilty'], [3, 'jkg']]
  lenumerate2('emilty jkg')
  Output:  [['emilty', 6], ['jkg', 3]] 
  lenumerate2('emilty jkg',False)
  Output:  [['emilty', 6], ['jkg', 3]]
"""
  



"""
Problem 4

Ex 4: Dictionary  

You have dictionary d with these names (as keys) and phone numbers (as values).
Ask user for a name, search the dict for this name (as key).
If the name exists as key in the dict, print out its phone numbers e.g. Jim 233-5467
If not, get the number for the name and add both to the dictionary,
then print out the full content.

"""
d = {'Jim':'233-5467', 'Bob':'643-7894', 'Anne':'478-4392', 'Jill':'952-4532'}

new=raw_input('Enter the query name:')
if(new in d):
  print 'Contact found. Phone number:',d[new]
  print 'Old List: ',d
else:
  number=raw_input('Contact not found. Enter the Phone number of contact: ')
  d[new]=number
  print 'Contact added. New list',d





"""
Problem 5

Ex 5: Objects, Assignment, reference, function call, argument, operators, in-place change

Answer the following questions in English in the spaces provided below.

[ 4 pts ]
"""

L1 = [334,43,75] 
print L1, id(L1)
# 1) What happens at the = ?
# Answer: A lvariable L1 is initialized toa list with three values [334,43,75]
Ouptut: [334, 43, 75] 43897800
where 43897800 is the identity of the object L1

# 2) What is [334,43,75]?
# Answer: It is a list with three items separated by a comma



L1 = L1 + [ len(L1) ]
print L1
# 3) Syntactically, what is something like + called in Python? (I know it's called a plus!)
# Answer: Concatenation operator
Output: [334, 43, 75, 3]


# 4) What is len() and what role has the L1 in len(L1)?
# Answer: len() is a built-in function, which computes the length of the object. In this case the length of the list L1 was 3 ( 3 values). Length(int) is conerted to a list by []. 
After concatenation, 3 (length of was added the list L1


L2 = L1
print L1, id(L1), L2, id(L2)
# 5) What relationship between L1 and L2 is created here?
# Answer: 
Output: [334, 43, 75, 3] 43897840 [334, 43, 75, 3] 43897840
L1 and L2 variables point to the same list hence have the same items and also have the same "identiy". 


L3 = L1[:]
print L3, id(L3), L1, id(L1), L2, id(L2)
# 6) What happens here? (how is this different from L3 = L1?)
# Answer: In this case slice [:] implies that our assigning specific items of one List into another new list ([:] implies all the items(slices) of L1 are initialized to L3) Also, both the variables L1 and L3 point to different lists implying that they(L1 and L3) have different identites. 
Output: [334, 43, 75, 3] 43897560 [334, 43, 75, 3] 43897840 [334, 43, 75, 3] 43897840


L2.sort() 
print L1, id(L1), L2, id(L2), L3, id(L3)
# 7) Why is L1 now also sorted but L3 is still unsorted? 
# Answer: Output: [3, 43, 75, 334] 43897840 [3, 43, 75, 334] 43897840 [334, 43, 75, 3] 43897560
Since variables L1 and L2 point to the same list, they would both be sorted, if one of them is sorted ans since L3 did not point to the same list, it was not sorted by the sorting operation on L2. 

print sorted(L3)
print L3, id(L3)
# 8) How does using sort() differ from sorted()?  
# Answer: Ouput: 
[3, 43, 75, 334]
[334, 43, 75, 3] 43897560

Firslty sort() is a method, sorted() is a buil-in function. Sort() method can only be used by lists, sorted() can be used for both tuples and lists (as tuples are immutable). We use sort on the list, for in-place sorting, and built in function sorted for not modifying the original list and returning a new sorted list




"""

Ex 6:  file conversion: read in, process and print out data

[ 3 pts ] Read the text file into a string and split into lines
[ 5 pts ] Put the records into a data structure
[ 2 pts ] Capitalize the sketch titles
[ 2 pts ] Sort the records alphabetically according to ID
[ 4 pts ] Print the table with a header row 
"""

# Task 1: Reading the file line by line
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()


print "Raw lines from text file:"
for l in lines: # list of strings, each containing a line from the text file
    print repr(l) # show internal representation of the list


# Task 2: Collect each record in a data structure
record={}
k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1
 
 OUTPUT:
  record
  {'ID=j8s74': ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=s4k5jk': ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 'ID=j234hg': ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 'ID=zd7u4h': ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 'ID=f983': ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)']}
  record['ID=j8s74'][0]
  'Date=15 September 1970'  
 
  
  


# Task 3: Convert all Titles to a titlecased (Capitalized) version
 for  i in record:
  record[i][1]=string.upper(record[i][1])
  
  OUTPUT:
   record
   {'ID=j8s74': ['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'TITLE=MR. PITHER'], 'ID=s4k5jk': ['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'], 'ID=j234hg': ['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU'], 'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'], 'ID=f983': ['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)']}
   
  
  


# Task 4: sort the records alphabetically according to ID
   newrecord={}
   for key in sorted(record):
    newrecord[key]=record[key]
   

# Task 5: print the sorted table on the console, make sure to line up the comumns with 
# one space in between ID, Date and Title, like shown below. Use string formatting and programatically
# determine the widest ID and widest Date beforehand (i.e. do not hardcode it to 8, loop through 
# all IDs and find out how many letters the longest ID has!)
# Also, no NOT just use a third party table formatter like prettytable or tabulate, use
+standard python only!

#ID     Date             Title
#f983   22 December 1970 Royal Episode 13 (Or: The Queen Will Be Watching)
#zd7u4h 19 October 1969  Bicycle Repair Man
#…	etc.

print '%-10s %-19s  Title'%('ID','Date')
for i in newrecord:
 print '%-10s %-19s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:],'\n'
 
 
OUTPUT:
 ID         Date                 Title
 j8s74      15 September 1970    THE SEMAPHORE VERSION OF WUTHERING HEIGHTS
 d45j5jkd   28 December 1969     THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM
 zd7u4h     19 October 1969      BICYCLE REPAIR MAN
 s4k5jk     8 December 1970      CROSSING THE ATLANTIC ON A TRICYCLE
 n4j6l3j    7 December 1972      MR. PITHER
 f983       22 December 1970     ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)
 j234hg     19 October 1969      COURT SCENE WITH CARDINAL RICHELIEU 