

# import the functions used from their modules 

# this does NOT import the entire module but only specific functions! However,
# it imports them directly into the current name space so you don't have to
# call them with their module name in front, e.g. isdir() instead of os.path.isdir() 
# if you want to use other functions defined in os or os.path, add them
# to the imports listed below in the same way.
from glob import glob
from os.path import exists, isdir, isfile, getsize, basename, join, split
from os import sep, getcwd, walk, listdir, chdir
 


"""
Problem 1


Define a function get_folder_names() that asks the user to enter the names of two folders as strings. 
    
    Check that folder1 and folder2 are valid sub-folders within the 
    current folder, i.e. it exists and that it is a folder, not a file; and that both are not the same
    
    If one or both do not exist, go back and have the user re-enter the sub-folder names.
    If the names for both folder are valid, return them inside a list
    
[ 2 pts ] Prompt the user for the folder names
[ 2 pts ] Check that folder1 and folder2 are valids ub-folders within the current folder
"""

def get_folder_names():
    
    #Shows the user the content of the current folder.
    #Asks the user to enter the names of the first and the second folder (must be different!)
    #If those names are in facts folders inside the current folder (they could be files or not exist at all!), 
    #the two names are returned inside a list. In any other case, have the user repeat the input
    #(you can be brutal and just demand both of them again, even if one of them is actually ok ...)
    
    #Note that getcwd() return the full (absolute) path of a folder, but glob("*") will return the folder's 
    #content as relative paths!
    
    
    # List current files and folders in the current folder ("*" matches everything)
    print "The current folder is", getcwd() # getcwd() returns the path to the current folder
    files_and_folders = glob("*") # glob("*") will return a list of (relative) file/folder names, not their absolute path!
    print "It contains:\n", files_and_folders    
    
    # Get user input
    print "Enter the name of two folders in the current folder:"
    folder1 = raw_input("First folder: ") # get input from the user (raw_input)
    folder2 = raw_input("Second Folder: ") # get input from the user (raw_input)

    # check if folder1 and folder2 are valid sub-folders within the current folder (files_and_folders):
    
    # a) check that each of them actually exists  (potential user error)
    while (exists(folder1) is False) or (exists(folder2) is False) :
        if exists(folder1) is False:
            folder1 = raw_input("Folder 1 does not exist. Enter First Folder name again: ")
        if exists(folder2) is False:
            folder2 = raw_input("Folder 2 does not exist. Enter Second Folder name again: ")
   
    # b) check that each of them is a folder, not a file
    while (isdir(folder1) is False) or (isdir(folder2) is False):
        if isdir(folder1) is False:
            folder1 = raw_input("Folder 1 is not a folder. Enter First Folder name again: ")
        if isdir(folder2) is False:
            folder2 = raw_input("Folder 2 is not a folder. Enter Second Folder name again: ")    
        
    # c) check that they are not equal (i.e. that they are not same folder), again, potential user error
    
    while folder1 == folder2:
        print "First and Second Folder names are equal. Enter the name of two folders in the current folder, again:"
        folder1 = raw_input("First folder: ") 
        folder2 = raw_input("Second Folder: ")        
        while (isdir(folder1) is False) or (isdir(folder2) is False): #This check is required again to ensure that the entered folder names actually exist as folders
            if isdir(folder1) is False:
                folder1 = raw_input("Folder 1 is not a folder. Enter First Folder name again: ")
            if isdir(folder2) is False:
                folder2 = raw_input("Folder 2 is not a folder. Enter Second Folder name again: ")  
                
        #A second check, similar to part(b) is required in part(c) to ensure that the function accepts ONLY those folder names which actually exist.
        #In this code, the user has to re-enter only the folder name which is invalid.
        #So I'm not being brutal!
                
    # if there's a problem, give feedback to the user and have the user enter both again.
    # (yes, you can make it simple on yourself and ask to re-enter both, even if one
    # imput was in fact valid  ...)

   

    # Now that you're sure that folder1 and folder2 are valid, return them inside a list (or tuple)
    return [folder1, folder2]




"""
Problem 2

Define a function get_dups(folder1, folder2) that returns a list
    of duplicate filnames in folder1 and folder2, e.g. here
    get_dups("folderA", "folderB") should returns ["B.txt", "C.txt"].
    
    Remember that you can use split() (os.path.split()) to split a full path
    c:\HW6\folder1\A.txt into a folder part (c:\HW6\folder1) and a file part (A.txt)
    and that you should glue together path names using + and os.sep (<- has the correct slash) 

[ 8 pts ]
"""
def get_dups(folder1, folder2):
    
    ## folder1 and folder2 are names of subfolder within the current folder 
    ## ex: "folderA" and "folderB"
    ## make a list of strings containing the filenames of the files in each folder
    ## ex: files_in_folder1 would contain ["A.txt", "C.txt"] 
    ##     files_in_folder2 would contain ["A.txt", "B.txt"] 
    ## create and return a list that contains duplicates:
    ## ex: duplicate_files would contain ["A.txt"]
    ## note: you can use in to test:  "bla" in ["whatever", "stuff", "bla"] => true
    ## for extra credit, also test for equal file size in bytes
    # ???
    
    files_in_folder1 = listdir(folder1) #List of files in folder1
    files_in_folder2 = listdir(folder2) #List of files in folder2
        
    
    #To ensure that only file names are present in the list files_in_folder1
    chdir(folder1) #Moving into folder1
    f1path = getcwd()
    i=0
    while i<len(files_in_folder1):
        if isfile(files_in_folder1[i]) is False:
            del files_in_folder1[i]
        i += 1
    #In the above piece of code, if the list element is NOT a file, but a folder, then it is deleted from the list since we are looking only for matching files and not for folders
    
    chdir("..") #Moving back to the parent folder
    chdir(folder2) #Moving into folder2
    f2path = getcwd()
    #To ensure that only file names are present in the list files_in_folder2
    i=0
    while i<len(files_in_folder2):
        if isfile(files_in_folder2[i]) is False:
            del files_in_folder2[i]
        i += 1  
    
    
    #To check for duplicates and make a list of duplicates
    chdir("..")
    duplicate_files = [x for x in files_in_folder1 for y in files_in_folder2 if x==y and getsize(f1path + sep + x)==getsize(f2path + sep + y)]
    #The above code uses list comprehension to create a list of all elements which are present in both files_in_folder1 as well as files_in_folder2, only if they have the same name AND the same file size.
    
    #Solution for Problem 3 is incorporated in this code.
    
    return duplicate_files
 
# ----------------------------  MAIN part -------------------------------- 
    
# Note: I have hardcoded folder1 and folder2 to specific names to get you started, 
# however, once you've defined it, you'll need to replace the following 2 lines with 
# a way of setting folder1 and folder2 via your get_folder_names() !


# get user input
folder_names = get_folder_names() # uncomment after you've completed the get_folder_names() function

folder1 = folder_names[0] #Extracting name of folder1 from the returned value from the function get_folder_names()
folder2 = folder_names[1] #Similarly, for folder2

# run get_dups() with the two subfolders 
dups = get_dups(folder1, folder2)

# Print out those files that occur in both folders:
print folder1, "and", folder2, "contain these duplicate files:"
for fname in dups: 
    print fname,     
print 


"""
Problem 3

Optional:  Using getsize(), refine your get_dups() function so that files only
   count as duplicates if they also have the same size (in bytes). 

[ +3 pts ]
"""

#Solution for this Problem incorporated in code for get_dups() above.





[ +5 pts ]
"""
# function to return the cummulative size of all files inside all sub-folders in bytes 
def get_total_size(folder):
    total_size_in_bytes = 0 
    # ???
    # add up sizes of single files into total_size_in_bytes
    return total_size_in_bytes



