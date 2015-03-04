true = 0
while true == 0:
        try:
                age =  input ("how old are you ? ")
                if 0 <= age <= 2:
                        print "If your that old how are you typing this?"
                        true = 1
                elif  3 <= age <= 5:
                        print "your a toddler."
                        true = 1
                elif 6 <= age <= 8:
                        true = 1
                        print "your a little kid."
                elif 9 <= age <= 10:
                        true = 1
                        print "your a kid."
                elif 11 <= age <= 12:
                        true = 1
                        print "your a pre-teen"
                elif 13 <= age <= 17:
                        true = 1
                        print "your a teen"
                elif 18 <= age <= 55:
                        true = 1
                        print "your an adult"
                else :
                        true = 1
                        print" your old"
        except:
                print"You can only enter numbers!!!"

