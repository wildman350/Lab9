############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

patients = (45)
while patients > 0:
    print "what is your temperature"
    hi = int(raw_input())
    if hi >= 105:
        print"you need to see a doctor!"
    if hi < 105 and hi < 98:
        print "have you been to africa? 1 for yes 2 for no"
    sick = int(raw_input())
    if sick == 1:
        print "you have ebola now you are going to die"
    if sick == 2:
        print "congrats youre not gonna die....yet" 
        print "have you been sick for more than 24 hours? 3 for yes 4 for no"
    userinput = int(raw_input())
    if userinput == 3:
        print "you should go and see a doctor"
    if userinput == 4:
        print "wait a little longer if you are still sick go see a doctor"
            