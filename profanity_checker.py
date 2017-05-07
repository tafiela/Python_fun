'''
I need to create a profanity checker for documents

the way i would approach it is as follow:

1- read a text
2- check for profanity

another website to test with is :  Pirate speech - http://isithackday.com/arrpi.php?text=friend
this website will convert normal text into Pirate speech

'''
import urllib


def read_file():
    
    fopen = open("/Users/mohammadouran/Documents/Python-workspace/Python_learning/Python-Fun/profanity.txt", "r+") #we are using the profanity.txt file in listdir
    fread = fopen.read()
    print fread 
    fopen.close()
    check_profanity(fread)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) #urlopen Helps open a connection to a URLand enables us to do things with it
    connection_response = connection.read()  #the response or output
    print "Profanity found : " + connection_response
    
    if "true" in connection_response:
        print "There is some profanity in this file!!!"
    elif "false" in connection_response:
        print "file looks clean!"
    else:
        print "No input to check!"
    connection.close()
    
    

read_file()