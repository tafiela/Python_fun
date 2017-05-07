'''

regex to memorise:

^  Begins with ...
$  Ends with ...


\d Represents any number
\D Represents anything but a number

\s Represents any space
\S Represents anything but a space

\w Represents any character
\W Represents anything but a character

.  Represents anything except a linebreak

\b Represents a space that proceeds or follows a whole word
    example :   My Dog  --> in this example if we used the \b we are referring to the space between "My" and "Dog"

*  Represents 0 or more repetitions

?  Represents 0 or 1

+  one or more of the regex that proceeds,
    example : \w+ one or more characters, \d one or more numbers
    
{n} Represents what the coder expects to see 
    example {n}\d{1,5} : the coder expects to see a 1-5 digits after the {n}

\e  Represents Escape

\f Form Feed

\n New Line

\r Carriage Return

\t tab 


Exercise Example :

to find the dollar amount of a sale :

\$\d*\.\d{2}


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

you were given a task to find all addresses in a document

- the housing numbers could be anywhere from 1 digit to 5 digits (1 - 99999)
- the road name
-with a period after the road name, street name or ave name.

example :

123 Main St. 

\d{1,5} you basically saying i expect 1,5 digits in length
\s   for space
\w+ you saying im expecting charcs and the + is for one or more
\s
\w+
\.    

'''
