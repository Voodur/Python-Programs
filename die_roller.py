# Die roller
# Created by Jeromie Rand for CSC 119
# Demonstrates using for loops and lists in Python

# Allows use of random numbers
import random

# Create an empty list
dice = []
#assign "straight" values
s1 = ([1,2,3,4,5])
s2 = ([2,3,4,5,6])
# Roll five dice (random numbers 1-6) and store each one in the list
for i in range(0,5):
    dice.append(random.randint(1,6))

# Print the dice that were rolled
print(dice)

# Create list to count the number of each die that showed up
# Initially, each value is zero
count = [0,0,0,0,0,0]
##
### Look at each die in the list
for die in dice:
# This lets us count how many of each value were rolled
# For example, if we rolled a 1, increment the value at count[0] by 1
    count[die-1] += 1 
    # You can uncomment this for debugging
    #print(die)
    #print(count)



# Finding the biggest number in the count list
# to determine if we rolled 2 of a kind, 3 of a kind, etc.
#"if" and "or" statements are added to determine a straight
if max(count) > 1:
    print('You had',max(count),'of a kind')         
    if dice == s1 or dice == s2:
        print('You got a straight!')
else:
    print('You had no pairs or better.')
