# This age script will behave the same as the other script

# Since True is always True the loop will run forever or until we call break
while True:
  try:
      age = input("How old are you? ")
  except:
      print "You can only enter numbers!!!"
      # continue will go to the start of the loop instead of continuing further
      continue
  if age < 0:
    print "You can't be younger than zero."
    continue
  if 0 <= age <= 2:
    print "If you're that old, how are you typing this?"
  elif  3 <= age <= 5:
    print "You're a toddler."
  elif 6 <= age <= 8:
    print "You're a little kid."
  elif 9 <= age <= 10:
    print "You're a kid."
  elif 11 <= age <= 12:
    print "You're a pre-teen."
  elif 13 <= age <= 17:
    print "You're a teen."
  elif 18 <= age <= 55:
    print "You're an adult."
  else:
    print" You're old."
  # break will stop the loop from running again
  break
