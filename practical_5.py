# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:09:49 2018

@author: gyojh
"""

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


# this is practical 5 from now on.

# reduce the code and make the number of agents more flexible- we can't cut and
# paste code if we have a million agents





# Import random and set a random number between 0-1
import random

import matplotlib.pyplot


random_number = random.random()
# Move y randomly
 


# Import and set a number at random between 0 and 99
agents = []

#after the imports we need to add a variable
num_of_agents = 10
#define the number of iterations
num_of_iterations = 100

# instead of assigning y0 and x0 with all the hassel on the last list, we can 
# assign the x and y with both random numbers, in this code below, the list 
# already knows
# where the x and the y go , so there's no need to define them, or create them:

#this creates one new set of co-ords, if we put this into a for-loop we can
# create as many agents as we like

for i in range (num_of_agents):
        agents.append([random.randint(0,99), random.randint(0,99)])

# this moves the x and y co-ords twice
# move x co-rd once 
#if random.random() < 0.5:
#    agents[0][0] += 1
#else:
#    agents[0][0] -= 1
# move y co-ord once
#if random.random() < 0.5:
#    agents[0][1] += 1
#else:
#    agents[0][1] -= 1
# move x co-ord again
#if random.random() < 0.5:
#    agents[0][0] += 1
#else:
#    agents[0][0] -= 1
## move y co-ord again
#if random.random() < 0.5:
#    agents[0][1] += 1
#else:
#    agents[0][1] -= 1

# this above only moves the x and y coord in one agent twice, we need to move 
# all the agents:
# here we move the agents by their x and y co-ords once in one run
#for i in range(num_of_agents):
#    if random.random() < 0.5:
#        agents [i][0] += 1
#        agents [i][1] += 1
#    else:
#        agents [i][0] -= 1
#        agents [i][1] -= 1
#    if random.random() < 0.5:
#        agents [i][0] += 1
#        agents [i][1] += 1
#    else:
#        agents [i][0] -= 1
#        agents [i][1] -= 1
        
#this is a repeat of above instead = num_of_iterations
# this moves the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:  
            #if its less that 0.5, it's itself + 1 on the x axis
            agents[i][0] = (agents[i][0] + 1) % 100
            #if it's less than 0.5, it's itself -1 on the x axis
            agents[i][0] = (agents[i][0] - 1) % 100
        else:
             #if its less that 0.5, it's itself + 1 on the y axis
            agents[i][1] = (agents[i][1] + 1) % 100
             #if its less that 0.5, it's itself + 1 on the y axis
            agents[i][1] = (agents[i][1] - 1) % 100
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
# and then we do it again 





