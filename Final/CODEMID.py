2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
Python Type "help", "copyright", "credits" or "license" for more information.
def lenumerate2(s,flip=None):
 if (flip=None|False)
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

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 10
def lenumerate2(s,flip=None):
 if (flip==None|False)
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

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 23
def lenumerate2(s,flip=None):
 if (flip==None|False)
  

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 23
def lenumerate2(s,flip=None):
 if(flip==None|False)

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 22

def lenumerate2(s,flip=None):
 if (flip==None|False):
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



lenumerate2('emily lkl')
Traceback (most recent call last):
  File "C:\Program Files (x86)\Wing IDE 101 5.1\src\debug\tserver\_sandbox.py", line 1, in <module>
    # Used internally for debug sandbox under external interpreter
  File "C:\Program Files (x86)\Wing IDE 101 5.1\src\debug\tserver\_sandbox.py", line 2, in lenumerate2
    if __name__ == '__main__':
TypeError: unsupported operand type(s) for |: 'NoneType' and 'bool'
lenumerate2('emily lkl',True)
Traceback (most recent call last):
  File "C:\Program Files (x86)\Wing IDE 101 5.1\src\debug\tserver\_sandbox.py", line 1, in <module>
    # Used internally for debug sandbox under external interpreter
  File "C:\Program Files (x86)\Wing IDE 101 5.1\src\debug\tserver\_sandbox.py", line 2, in lenumerate2
    if __name__ == '__main__':
TypeError: unsupported operand type(s) for |: 'NoneType' and 'bool'
def lenumerate2(s,flip=None):
 if ((flip=None)or(flip=False)):
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

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 11

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


lenumerate2('emilty jkg',True)
Output:  [[6, 'emilty'], [3, 'jkg']]
lenumerate2('emilty jkg')
Output:  [['emilty', 6], ['jkg', 3]]
lenumerate2('emilty jkg',False)
Output:  [['emilty', 6], ['jkg', 3]]
count=6
print count
6
count=0
for i in F
 for a in N
   if(i==a)
    count+=1
 print i+' occurs in N '+count+ ' times\n'
 count=0

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 11
count=0
for i in F:
 for a in N:
   if(i==a):
    count+=1
 print i+' occurs in N '+count+ ' times\n'
 count=0

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
NameError: name 'F' is not defined
F = [4,7,2]
N = [2,3,4,2,5,6,3,2,6,7,3,4]

count=0
for i in F
 for a in N
   if(i==a)
    count+=1
 print i+' occurs in N '+count+ ' times\n'
 count=0

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
invalid syntax: <string>, line 2, pos 11
count=0
for i in F:
 for a in N:
   if(i==a):
    count+=1
 print i+' occurs in N '+count+ ' times\n'
 count=0

Traceback (most recent call last):
  File "<string>", line 6, in <fragment>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print 'df+5
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
EOL while scanning string literal: <string>, line 1, pos 11
print 'df'+5
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: cannot concatenate 'str' and 'int' objects
count=5
print 'count',count
count 5
count=0
for i in F:
 for a in N:
   if(i==a):
    count+=1
 print i,' occurs in N ',count,' times\n'
 count=0

4  occurs in N  2  times

7  occurs in N  1  times

2  occurs in N  3  times

r=print'raw_input('enter vlaue')'
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 7
print'raw_input('enter vlaue')'
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 22
k=raw_input('Enter value')
Enter value6
k
'6'
d = {'Jim':'233-5467', 'Bob':'643-7894', 'Anne':'478-4392', 'Jill':'952-4532'}

new=raw_input('Enter the query name:')
if(new in d):
  print 'Contact found. Phone number:',tel[new]
  print 'List',d
else:
  number=raw_input('Contact not found. Enter the Phone number of contact: ')
  d[new]=number
  print 'Contact added. New list',d

Enter the query name:Bob
Contact found. Phone number:Traceback (most recent call last):
  File "<string>", line 5, in <fragment>
NameError: name 'tel' is not defined
new=raw_input('Enter the query name:')
if(new in d):
  print 'Contact found. Phone number:',d[new]
  print 'List',d
else:
  number=raw_input('Contact not found. Enter the Phone number of contact: ')
  d[new]=number
  print 'Contact added. New list',d

 Enter the query name:Bob
Contact found. Phone number: 643-7894
List {'Jill': '952-4532', 'Bob': '643-7894', 'Jim': '233-5467', 'Anne': '478-4392'}
new=raw_input('Enter the query name:')
if(new in d):
  print 'Contact found. Phone number:',d[new]
  print 'List',d
else:
  number=raw_input('Contact not found. Enter the Phone number of contact: ')
  d[new]=number
  print 'Contact added. New list',d

Enter the query name:James
Contact not found. Enter the Phone number of contact: 545-45
Contact added. New list {'Jill': '952-4532', 'Bob': '643-7894', 'Jim': '233-5467', 'Anne': '478-4392', 'James': '545-45'}
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()

Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
IOError: [Errno 2] No such file or directory: 'database.txt'
getcwd()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'getcwd' is not defined
import os
getcwd()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'getcwd' is not defined
os getcwd()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 9
os cwd()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 6
os.getcwd()
'C:\\Users\\vssc1_000\\Downloads'
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()

lines
['ID=j234hg', 'Date=19 October 1969', 'Title=court scene with cardinal richelieu', 'ID=d45j5jkd', 'Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM', 'ID=s4k5jk', 'Date=8 December 1970', 'Title=crossing the atlantic on a tricycle', 'ID=zd7u4h', 'Date=19 October 1969', 'Title=Bicycle Repair Man', 'ID=f983', 'Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)', 'ID=j8s74', 'Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS', 'ID=n4j6l3j', 'Date=7 December 1972', 'Title=Mr. Pither']
d['dfl']=[1,5]
d
{'James': '545-45', 'Jim': '233-5467', 'dfl': [1, 5], 'Jill': '952-4532', 'Bob': '643-7894', 'Anne': '478-4392'}
lines
['ID=j234hg', 'Date=19 October 1969', 'Title=court scene with cardinal richelieu', 'ID=d45j5jkd', 'Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM', 'ID=s4k5jk', 'Date=8 December 1970', 'Title=crossing the atlantic on a tricycle', 'ID=zd7u4h', 'Date=19 October 1969', 'Title=Bicycle Repair Man', 'ID=f983', 'Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)', 'ID=j8s74', 'Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS', 'ID=n4j6l3j', 'Date=7 December 1972', 'Title=Mr. Pither']
for i in lines
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 15
a=['a','f','d']
for i in a
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 11
for i in a:
 print i+1

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
TypeError: cannot concatenate 'str' and 'int' objects
for i in a:
 print a.index(i+1)

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
TypeError: cannot concatenate 'str' and 'int' objects
for i in a:
 print a.index(i)

0
1
2
g['fg']=[1,2]
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'g' is not defined

g={}
g['fg']=[1,2]
g
{'fg': [1, 2]}
g['fg']
[1, 2]
g['fg[0]']
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
KeyError: 'fg[0]'
g['fg'][0]
1
for in in range(5)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 6
for in in range(5):
 print i

Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 6
for i in range(5)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 18
for i in range(5):
 print i

0
1
2
3
4
for i in range(5):
 print i
 i+=1

0
1
2
3
4
for i in range(5):
 print i
 i=3

0
1
2
3
4
for i+1 in range(5):
 print i

Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
can't assign to operator: <string>, line 1
for i+1 in range(5):
 print i

Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
can't assign to operator: <string>, line 1
j=10/5+2
j
4
while(j--)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 10
while(j-=0)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 9
k=len(lines)/3
i=0
while(k):      
 record[i]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

Traceback (most recent call last):
  File "<string>", line 4, in <fragment>
NameError: name 'record' is not defined
record={}
k=len(lines)/3
i=0
while(k):      
 record[i]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

record
{0: ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 3: ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 6: ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 9: ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 12: ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)'], 15: ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 18: ['Date=7 December 1972', 'Title=Mr. Pither']}
k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1


record
{0: ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 'ID=j8s74': ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 3: ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 6: ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 9: ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 12: ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)'], 15: ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 18: ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=s4k5jk': ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 'ID=n4j6l3j': ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=zd7u4h': ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 'ID=f983': ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)'], 'ID=j234hg': ['Date=19 October 1969', 'Title=court scene with cardinal richelieu']}
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()

record={}
k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

record
{'ID=j8s74': ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=s4k5jk': ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 'ID=j234hg': ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 'ID=zd7u4h': ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 'ID=f983': ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)']}
record['ID=j8s74'][0]
'Date=15 September 1970'
t='sarat'
t.uppercase
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
AttributeError: 'str' object has no attribute 'uppercase'
str='sarat'
str.uppercase
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
AttributeError: 'str' object has no attribute 'uppercase'
k=string.uppercase(str)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'string' is not defined
import string
k=string.uppercase(str)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: 'str' object is not callable
k=string.uppercase(t)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: 'str' object is not callable
s='sads'
string.upper(s)
'SADS'
s='sadS'
string.upper(s)
'SADS'
s
'sadS'
lines.sort()
lines
['Date=15 September 1970', 'Date=19 October 1969', 'Date=19 October 1969', 'Date=22 December 1970', 'Date=28 December 1969', 'Date=7 December 1972', 'Date=8 December 1970', 'ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h', 'Title=Bicycle Repair Man', 'Title=Mr. Pither', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS', 'Title=court scene with cardinal richelieu', 'Title=crossing the atlantic on a tricycle']
record.sort()
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
AttributeError: 'dict' object has no attribute 'sort'
sorted(record)
['ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h']
record
{'ID=j8s74': ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=s4k5jk': ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 'ID=j234hg': ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 'ID=zd7u4h': ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 'ID=f983': ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)']}
record=sorted(record)
record
['ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h']
from sortedcontainers import SortedDict
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
ImportError: No module named sortedcontainers
import SortedDict
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
ImportError: No module named SortedDict
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()

lines
['ID=j234hg', 'Date=19 October 1969', 'Title=court scene with cardinal richelieu', 'ID=d45j5jkd', 'Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM', 'ID=s4k5jk', 'Date=8 December 1970', 'Title=crossing the atlantic on a tricycle', 'ID=zd7u4h', 'Date=19 October 1969', 'Title=Bicycle Repair Man', 'ID=f983', 'Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)', 'ID=j8s74', 'Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS', 'ID=n4j6l3j', 'Date=7 December 1972', 'Title=Mr. Pither']
k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

Traceback (most recent call last):
  File "<string>", line 4, in <fragment>
TypeError: list indices must be integers, not str
df={'sape': 4139, 'guido': 4127, 'jack': 4098}
df=df+{'gh':'ui'}
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print 'uj %0.5dgh'
uj %0.5dgh
print 'uj %0.5d',ghg
uj %0.5dTraceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'ghg' is not defined
print 'uj %0.5d',6
 uj %0.5d 6
print 'uj %0.5d'6
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 17
print 'uj %5d',6
uj %5d 6
print 'uj %5d',(6)
uj %5d 6
print 'uj %5d',%(6)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
invalid syntax: <string>, line 1, pos 16
print 'uj %5d' %6
uj     6
print 'uj %-5d',(6)
uj %-5d 6
print 'uj %-5d' %6
uj 6    
print 'uj %-5djk' %6
uj 6    jk

print '%-10s %-15%s Title'%('ID','Date')

Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: not all arguments converted during string formatting
print '%-10s %-15s Title'%('ID','Date')
ID         Date            Title
infile = open("database.txt")
full_text = infile.read() #String display of the text file
lines = full_text.split('\n')  # Every line in the text becomes a item in the list
infile.close()

k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

Traceback (most recent call last):
  File "<string>", line 4, in <fragment>
TypeError: list indices must be integers, not str
record={}
k=len(lines)/3
i=0
while(k):      
 record[lines[i]]=[lines[i+1],lines[i+2]]
 i=i+3
 k-=1

record
{'ID=j8s74': ['Date=15 September 1970', 'Title=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'Title=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'Title=Mr. Pither'], 'ID=s4k5jk': ['Date=8 December 1970', 'Title=crossing the atlantic on a tricycle'], 'ID=j234hg': ['Date=19 October 1969', 'Title=court scene with cardinal richelieu'], 'ID=zd7u4h': ['Date=19 October 1969', 'Title=Bicycle Repair Man'], 'ID=f983': ['Date=22 December 1970', 'Title=Royal Episode 13 (or: The Queen Will Be Watching)']}
for  i in lines:
 record[i][1]=string.upper(record[i][1])

Traceback (most recent call last):
  File "<string>", line 2, in <fragment>
KeyError: 'Date=19 October 1969'
for  i in record:
 record[i][1]=string.upper(record[i][1])

record
{'ID=j8s74': ['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=n4j6l3j': ['Date=7 December 1972', 'TITLE=MR. PITHER'], 'ID=s4k5jk': ['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'], 'ID=j234hg': ['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU'], 'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'], 'ID=f983': ['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)']}
newrecord={}
for key in sorted(record):
 newrecord[key]=record[key]

newrecord
{'ID=j8s74': ['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'], 'ID=s4k5jk': ['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'], 'ID=n4j6l3j': ['Date=7 December 1972', 'TITLE=MR. PITHER'], 'ID=f983': ['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)'], 'ID=j234hg': ['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU']}
soreted(record)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
NameError: name 'soreted' is not defined
sorted(record)
['ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h']
k=sorted(record)
k
['ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h']
newrecord={}
for key in k:
 newrecord[key]=record[key]

newrecord
{'ID=j8s74': ['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'], 'ID=s4k5jk': ['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'], 'ID=n4j6l3j': ['Date=7 December 1972', 'TITLE=MR. PITHER'], 'ID=f983': ['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)'], 'ID=j234hg': ['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU']}
newrecord={}
for key in k:
 newrecord={key:record[key]}

newrecord
{'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN']}
k=sorted(record.keys)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: 'builtin_function_or_method' object is not iterable
k=sorted(record.keys())
k
['ID=d45j5jkd', 'ID=f983', 'ID=j234hg', 'ID=j8s74', 'ID=n4j6l3j', 'ID=s4k5jk', 'ID=zd7u4h']
record.key(0)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
AttributeError: 'dict' object has no attribute 'key'
record.keys(0)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: keys() takes no arguments (1 given)
newrecord={}
for key in sorted(record):
 newrecord[key]=record[key]

newrecord
{'ID=j8s74': ['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'], 'ID=d45j5jkd': ['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'], 'ID=zd7u4h': ['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'], 'ID=s4k5jk': ['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'], 'ID=n4j6l3j': ['Date=7 December 1972', 'TITLE=MR. PITHER'], 'ID=f983': ['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)'], 'ID=j234hg': ['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU']}
print '%-10s %-15s Title'%('ID','Date')
for i in newrecord:
 print '%-10s %-15s '%(newrecord[i],newrecord[i][0]),newrecord[i][1],'\n'

ID         Date            Title
['Date=15 September 1970', 'TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS'] Date=15 September 1970  TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

['Date=28 December 1969', 'TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM'] Date=28 December 1969  TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

['Date=19 October 1969', 'TITLE=BICYCLE REPAIR MAN'] Date=19 October 1969  TITLE=BICYCLE REPAIR MAN 

['Date=8 December 1970', 'TITLE=CROSSING THE ATLANTIC ON A TRICYCLE'] Date=8 December 1970  TITLE=CROSSING THE ATLANTIC ON A TRICYCLE 

['Date=7 December 1972', 'TITLE=MR. PITHER'] Date=7 December 1972  TITLE=MR. PITHER 

['Date=22 December 1970', 'TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)'] Date=22 December 1970  TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

['Date=19 October 1969', 'TITLE=COURT SCENE WITH CARDINAL RICHELIEU'] Date=19 October 1969  TITLE=COURT SCENE WITH CARDINAL RICHELIEU 

for i in newrecord:
 print '%-10s %-15s '%(i,newrecord[i][0]),newrecord[i][1],'\n'

ID=j8s74   Date=15 September 1970  TITLE=THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

ID=d45j5jkd Date=28 December 1969  TITLE=THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

ID=zd7u4h  Date=19 October 1969  TITLE=BICYCLE REPAIR MAN 

ID=s4k5jk  Date=8 December 1970  TITLE=CROSSING THE ATLANTIC ON A TRICYCLE 

ID=n4j6l3j Date=7 December 1972  TITLE=MR. PITHER 

ID=f983    Date=22 December 1970  TITLE=ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

ID=j234hg  Date=19 October 1969  TITLE=COURT SCENE WITH CARDINAL RICHELIEU 

for i in newrecord:
 print '%-10s %-15s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:],'\n'

j8s74      15 September 1970  THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

d45j5jkd   28 December 1969  THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

zd7u4h     19 October 1969  BICYCLE REPAIR MAN 

s4k5jk     8 December 1970  CROSSING THE ATLANTIC ON A TRICYCLE 

n4j6l3j    7 December 1972  MR. PITHER 

f983       22 December 1970  ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

j234hg     19 October 1969  COURT SCENE WITH CARDINAL RICHELIEU 

print '%-10s %-19s Title'%('ID','Date')
for i in newrecord:
 print '%-10s %-19s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:],'\n'

ID         Date                Title
j8s74      15 September 1970    THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

d45j5jkd   28 December 1969     THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

zd7u4h     19 October 1969      BICYCLE REPAIR MAN 

s4k5jk     8 December 1970      CROSSING THE ATLANTIC ON A TRICYCLE 

n4j6l3j    7 December 1972      MR. PITHER 

f983       22 December 1970     ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

j234hg     19 October 1969      COURT SCENE WITH CARDINAL RICHELIEU 

print '%-10s %-19s Title'%('ID','Date')
for i in sorted(newrecord):
 print '%-10s %-19s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:],'\n'

ID         Date                Title
d45j5jkd   28 December 1969     THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

f983       22 December 1970     ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

j234hg     19 October 1969      COURT SCENE WITH CARDINAL RICHELIEU 

j8s74      15 September 1970    THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

n4j6l3j    7 December 1972      MR. PITHER 

s4k5jk     8 December 1970      CROSSING THE ATLANTIC ON A TRICYCLE 

zd7u4h     19 October 1969      BICYCLE REPAIR MAN 

print '%-10s %-19s  Title'%('ID','Date')
for i in newrecord:
 print '%-10s %-19s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:],'\n'

ID         Date                 Title
j8s74      15 September 1970    THE SEMAPHORE VERSION OF WUTHERING HEIGHTS 

d45j5jkd   28 December 1969     THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM 

zd7u4h     19 October 1969      BICYCLE REPAIR MAN 

s4k5jk     8 December 1970      CROSSING THE ATLANTIC ON A TRICYCLE 

n4j6l3j    7 December 1972      MR. PITHER 

f983       22 December 1970     ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING) 

j234hg     19 October 1969      COURT SCENE WITH CARDINAL RICHELIEU 

print '%-10s %-19s  Title'%('ID','Date')
for i in newrecord:
 print '%-10s %-19s '%(i[3:],newrecord[i][0][5:]),newrecord[i][1][6:]

ID         Date                 Title
j8s74      15 September 1970    THE SEMAPHORE VERSION OF WUTHERING HEIGHTS
d45j5jkd   28 December 1969     THE ROYAL PHILHARMONIC ORCHESTRA GOES TO THE BATHROOM
zd7u4h     19 October 1969      BICYCLE REPAIR MAN
s4k5jk     8 December 1970      CROSSING THE ATLANTIC ON A TRICYCLE
n4j6l3j    7 December 1972      MR. PITHER
f983       22 December 1970     ROYAL EPISODE 13 (OR: THE QUEEN WILL BE WATCHING)
j234hg     19 October 1969      COURT SCENE WITH CARDINAL RICHELIEU
