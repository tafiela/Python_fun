'''
The goals of this program is to rename a list of files in a specific folder

my approach on this is:

1st - need to get the files from the specific folder
2nd - add them to a list
3rd- for every filename rename 

'''

import os

Current_working_directoty = os.getcwd()
print "Our current working directory is " + Current_working_directoty

print "\n\nLets change our working directory to the folder where the files are : "
os.chdir("/Users/mohammadouran/Documents/Python-workspace/Python_learning/Python-Fun/Use functions Videos/prank_files_excercise/")

print "\nChnaged!!! to "

print "Current working directory is : " + Current_working_directoty


def file_rename():
    
    file_list = os.listdir("/Users/mohammadouran/Documents/Python-workspace/Python_learning/Python-Fun/Use functions Videos/prank_files_excercise/")

    for file in file_list:
        #os.rename(current_file_name, New name)
        #file.translate(table, charcters_to_be_removed)
        print "Old File Name - " + file
        print "New File Name - " + file.translate(None, "1234567890")
        os.rename(file, file.translate(None, "1234567890"))
        
    print file_list
        
      
file_rename()


