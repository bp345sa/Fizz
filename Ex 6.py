# assigning a string to variable x
x = "There are %d types of people." % 10
#assigning a string to variable binary
binary = "binary"
#assigning a string to variable do_not
do_not = "don't"
#printing strings assigned to variable within another string
#string within a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#string within a string
print "I said: %s." % x
#string within a string
print "I also said: %s." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %s"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

