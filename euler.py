from math import e
val = input("Enter Function: ")
step_size = input("Enter step-size: ")
find = input("Enter function you are looking for: ")
word = ""
for letter in find:
    if letter in ".1234567890":
        word += letter
find = word

if "^" in val:
    val = val.replace("^", "**")


init_y = input("Enter your initial y: ")
init_x = input("Enter your initial x: ")
#Using the entered function get the value of y after you reach 'find'
#with number of steps (using step-size)

#Idea: From initial x (entered) to 'find', y should equal the formula?
#How can I do this recursively



def eulerOne(f,x,y,size,find_a):
    if "y" and "x" in f:
        function = lambda x, y: eval(f)
    elif "x" in f and not("y" in f):
        function = lambda x: eval(f)
    else:
        function = lambda y: eval(f)

    try:
        y = y + (size * float(function(x,y)))
    except TypeError:
        try:
            y = y + (size * float(function(x)))
        except:
            y = y + (size * float(function(y)))


    if find_a == (x + size):
        return y
    else:
        next = x + size
        return eulerOne(f,next, y, size, find_a)

print(round(eulerOne(val, float(init_x), float(init_y), float(step_size), float(find)),3))
