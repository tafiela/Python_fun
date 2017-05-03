'''
Write a program that reminds you every two hours to take a break from working
the program will open a youtube video for the break, and after the video you can resume working 
until another two hours breaker

how will you do it?

- need to turn on a timer for every 2 minutes 
- once times is up we need to play the youtube video

this will happen mulitple times during the working day, since there is 3 occasions for the video to play


'''
import datetime 
import time 
import webbrowser

initial_time = datetime.datetime.now()
url = "https://www.youtube.com/watch?v=a3HZ8S2H-GQ" #this is the url that will open

breaks = 0


print "You started work at {}-{}-{}, on {}/{}/{}".format(initial_time.hour, initial_time.minute, initial_time.second, initial_time.day, initial_time.month, initial_time.year)

while breaks < 3:

   
    
#     [SOLUTION NUMBER 1 ] 
#     This will start and print a countdown 
    print "ATTENTION : System going on break in: "
    for i in xrange((60*2),0,-1): #starting a countdown from 10, until 0 [0 not included] by the decrements of -1
        time.sleep(1) #wait 1 second before printing the new iteration
        print i 
    
    
#     #[SOLUTION NUMBER 2 ]
#     #this will not print the countdown 
#     
#     time.sleep(2*60) #This will wait for 120 secons before it goes to the below step of opening the browser
#     
    time.sleep(1) #wait one second before opening the browser

    webbrowser.open(url) 
    breaks +=1
    
 
    
    






