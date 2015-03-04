# I wouldn't use true for a variable, its confusing as boolean True already exists
# https://docs.python.org/2/library/constants.html
# https://docs.python.org/2/library/functions.html#bool

true = 0
while true == 0:
        try:
                age =  input ("How old are you? ")
                if 0 <= age <= 2:
                        print "If you're that old, how are you typing this?"
                        true = 1
                elif  3 <= age <= 5:
                        print "You're a toddler."
                        true = 1
                elif 6 <= age <= 8:
                        true = 1
                        print "You're a little kid."
                elif 9 <= age <= 10:
                        true = 1
                        print "You're a kid."
                elif 11 <= age <= 12:
                        true = 1
                        print "You're a pre-teen."
                elif 13 <= age <= 17:
                        true = 1
                        print "You're a teen."
                elif 18 <= age <= 55:
                        true = 1
                        print "You're an adult."
                else :
                        true = 1
                        print" You're old."
        except:
                print"You can only enter numbers!!!"

