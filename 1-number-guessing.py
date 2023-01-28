# Number guessing game ranged 1-100
## Goal: Randomly generate a list from 1-100, with the size of 20. A number will get picked for answer.
# Fail Attempt: The output will narrow the range of correct number
# Successful Attempt: Output Congrats message and exit


import numpy as np
from numpy import random
import sys


#Verify input ranged from 1-100 (Integer)
def number_checker(input):
    try:
        val = int(input)
        if val > 0 and val <=100:
            return True
        else:
            print("Plese enter a number ranged 1-100")
            return False
    except ValueError:
        try:
            val = float(input)
            print("This is a float number. Please enter an integer ranged 1-100")
            return False
        except ValueError:
            print("This is a String. Please enter an integer ranged 1-100")
            return False



#Eliminate half the array because of incorrect guess. 
def cal(list1, pos1, pos2):

        # print("pos1 = ", pos1 ,"pos2 = ", pos2,"list1[pos1] = ", list1[pos1], "list1[pos2] = ", list1[pos2] )
        if (list1[pos2]<list1[pos1] and pos2 < pos1):
            del list1[pos1:]
        elif (list1[pos2]>list1[pos1] and pos2 > pos1):
            del list1[:pos1]
        elif (list1[pos2]==list1[pos1]):
            del list1[pos2+1:]
        # print("Remaining Items:", list1[:])
        return list1



#Allow userinput
def userinput():
    checker = False
    while (checker == False):
        input1 = input()
        checker = number_checker(input1)
    return int(input1)



# Main Function
# Putting 20 random numbers with no duplication and sort the list
# Define the target number
list1 = list(np.random.permutation(np.arange(0,100))[:20])
list1_sorted = sorted(list1)
pickup = random.randint(20)
Target = list1_sorted[pickup]


# Welcoming message
print("Welcome to number guessing game!")
print("Please enter your guess. Range 1-100")


#Verify input ranged from 1-100 (Integer)
input1 = userinput()


if (Target == input1):
    print("Congrats!! You have a RIGHT GUESS!")
    sys.exit()


#Narrow the range for next guess
while (Target!= input1):
        pos1 = int(len(list1_sorted)/2)
        pos2 = list1_sorted.index(Target)
        list1_sorted = cal(list1_sorted, pos1, pos2)
        print("Please try another guess. Range from", list1_sorted[0], " to ", list1_sorted[len(list1_sorted)-1])
        input1 = userinput()


print("Congrats!! You have a RIGHT GUESS!")