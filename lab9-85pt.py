############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]

# Insert for loop here


# This should print [102,101,103,105]

mylist = (102,98,96,101,100,99,103,97,98,105)
mylistGreaterthan100 = []
for x in mylist:
    if x >100:
        mylistGreaterthan100.append(x)
print mylistGreaterthan100
