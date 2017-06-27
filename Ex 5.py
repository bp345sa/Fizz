name = 'Zed A. Shaw'
age = 23 # not a lie
height = 74 # inches
h1 = height * 2.54
weight = 180 # lbs
w1 = weight * 0.456
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f centimetres tall." % h1
print "He's %f kilograms heavy." % w1
print "Actually that's not too heavy."
print "He's got %r eyes and %r" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %f, and %f I get %f." % (age, h1, w1, age + h1 + w1)

