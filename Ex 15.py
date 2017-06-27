#imports filename as argument variable
from sys import argv

#assigns two seperate variables into argument variable 
script = argv

#opens the sample .txt file
print "Enter the name of the file: "
filename = raw_input()
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()


