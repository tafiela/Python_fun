'''
map is a cool function in python that allows you to map a function to a list

filter is a function that returns the elements that resulted in True in its argument function against a list

'''

#To test the map function 
a=range(1,30)
b=[]


def double_numb(x):
    return x*2

rootit = lambda x : x**2  #writting a function with lambda
    
print "This is to test the map function : "        
print map(double_numb, a)
print map(rootit,a)
print "\n\n"

#To test the filter function

print "This is to test the filter function : "

c=range(31, 60)

def find_even(x):
    return x % 2 == 0

odd_num = lambda x: x%2 == 1 #writting a function with lambda


print filter(find_even, c) #it returned only if the find_even returned True 
print filter(odd_num, c)