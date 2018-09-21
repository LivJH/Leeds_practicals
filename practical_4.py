# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:00:28 2018

@author: gyojh
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:42:25 2018

@author: gyojh
"""
# Set up variable
y0 = 50
x0 = 50
## this makes a copy of model.py so it can be used for this prac


# Import random and set a random number between 0-1
import random

#import operator for the second part
import operator

#import matplotlib.pyplot
import matplotlib.pyplot

random_number = random.random()
# Move y randomly
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1
# copy
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1   

# Move x randomly
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1
# copy
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1    


# Set up variable
y1 = 50
x1 = 50

#Import and set a random number
random_number = random.random()
# Move 
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1   

if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1    
 
# this will then work out the distance between x and y 
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
answer = sum**0.5


# Import and set a number at random between 0 and 99
agents = []


# instead of assigning y0 and x0 with all the hassel on the last list, we can 
# assign the x and y with both random numbers, in this code below, the list 
# already knows
# where the x and the y go , so there's no need to define them, or create them:
agents.append([random.randint(0,99), random.randint(0,99)])

# this adds our first set of co-ords, the extra sq brackets add co-ords 
# as a list inside another list. Here is a 2D data set, in the first dimension
# agents[0]  represents each agent and the second dimension is the 2 co-ords. 
# agents [0] [0] is the y co-ord because the first 0 is the first list (there's
#only one) and the second 0 is the first character in the first list which is 
# y0. 

# print
print(agents)

random_number = random.random()
# Move y0 randomly, this is now assigned as agents[0][0]
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1   

# Move x randomly
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1    
# prints both x and y distance    
print (y0, x0)





agents.append([random.randint(0,99), random.randint(0,99)])

#Import and set a random number
random_number = random.random()
# Move 
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1   

if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1    
    
print (y1, x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
answer = sum**0.5
print(answer)




# this has got rid of the y0 and x0 from the previous practical
# however we havent muched reduced our code yet





# containers practical, this will find out which agent is further east, or the 
# or the larger x. so we have to use the function max() 


 # max will run through the list of agents co-ords to work out the largest. 
 # remeber that the first value in the list is the y and the second value in 
 # the list is an x
print (max(agents))
#this looks inside each square bracket, and finds the largest first value, or
# the one value on the left
print (max(agents, key=operator.itemgetter(0)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()

#to extract the largest right value, or x value:
x = max(agents, key=operator.itemgetter(1))
y = max(agents, key=operator.itemgetter(0))

matplotlib.pyplot.scatter(x,y, color='red')

matplotlib.pyplot.show()


#another way of finding the most largest easterly point is by doing this:

