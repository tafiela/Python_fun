import turtle #This programs draws pictures 


def draw_square():
    window =turtle.Screen() #we are adding a window screen that we will draw on, kinda like getting a piece of paper to draw on
    window.bgcolor("green") #the background color will be red here
    
    brad = turtle.Turtle() #this is how we initiate  the Turtle program 
    brad.color("Blue")
    brad.shape("turtle")
         
    x=0
    while x< 4:
#       '''
#       for i in range(1,5):
#       '''  
        brad.forward(100) #100 is the distance to draw
        brad.right(90)    #90 is the angle 
        x+=1
       
    window.exitonclick() #the method on how we will close the window we have been drawing on
   

def draw_circle():
    
    window =turtle.Screen() #we are adding a window screen that we will draw on, kinda like getting a piece of paper to draw on
    window.bgcolor("green") #the background color will be red here
    
    angie = turtle.Turtle()
    angie.color("Red")
    angie.circle(100)
    
    
    window.exitonclick() #the method on how we will close the window we have been drawing on
 
 
def draw_traingle():
    
    window =turtle.Screen() #we are adding a window screen that we will draw on, kinda like getting a piece of paper to draw on
    window.bgcolor("green") #the background color will be red here
    
    trick = turtle.Turtle()
    trick.color("Red")
    
    trick.right(45)
    trick.forward(150)
    trick.right(120)
    trick.forward(150)
    trick.right(120)
    trick.forward(152)
     
    window.exitonclick() #the method on how we will close the window we have been drawing on
 
 
def artsy():
    
    window =turtle.Screen() #we are adding a window screen that we will draw on, kinda like getting a piece of paper to draw on
    window.bgcolor("red") #the background color will be red here

    z=turtle.Turtle()
    z.speed(50)
    z.color("yellow")
    
    while True:
        
       z.right(10)
       
       z.forward(100)
       z.right(90)
       
       z.forward(100)
       z.right(90)
       
       z.forward(100)
       z.right(90)
       
       z.forward(100)
       z.right(90)

    
    window.exitonclick() #the method on how we will close the window we have been drawing on
    
    
artsy()
