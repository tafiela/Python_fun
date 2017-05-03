from datetime import datetime 

x="this is how we do it"
y= 123

print "%s when we want to add %d" %(x,y)
print "{} when we want to add {}".format(x,y) # you dont need to define if its a string or int with .format
 
t=dir(datetime)

print datetime.now()

# for i in t:
# 	print i
