def hello(): ## Whatever is in here is set as hello()
    print "Hello"
 
def area(w, h): ## What ever is here is set as area(w, h)
    return w * h ## return will print strings and ints. Here we print w X h
 
def print_welcome(name): ## here we print and make but not set name
    print "Welcome", name

hello() ## Here we use the first lines def
hello() ## Here we use the first lines def
print_welcome("Fred") ## here we use print_welcome("Fred") in order to define Fred and use def print_welcome()
w = 4
h = 5
print "width =", w, "\nheight =", h, "\narea =", area(w, h) ## i forgot to teach you \n didn't I/ \n make the following text go to the next line


