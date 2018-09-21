# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:12:27 2018

@author: gyojh
"""



import random

import matplotlib.pyplot

random_number = random.random()

### in this lesson we now want to get every pair and pass them into a function so that 
# we can tell how far they are apart
# note: we are changing agents [0] to agent row a- this decides which value on
#  to look at (below on line 69 i've chosen agent 4), and
#agent row b is the determines which other agent to look at (on line 64 i chose
# agent 7. This function then decides that one of the agents has to be subtracted
#from another to work out the distance. We choose which values we want in the 
#function starting from line 66
# we have to write the following function declaration
                                                            
def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return answer


# Move y randomly
 
# Import and set a number at random between 0 and 99
agents = []

#after the imports we need to add a variable
num_of_agents = 10
#define the number of iterations
num_of_iterations = 100


for i in range (num_of_agents):
        agents.append([random.randint(0,99), random.randint(0,99)])

        
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

# test the distance between the agents, this uses the new function at the top 
distance = distance_between(agents[0], agents[1])
print(distance)

distance = distance_between(agents[4], agents[7])
print(distance)

distance = distance_between(agents[3], agents[6])
print(distance)

#we now need to test every other agent against eachother and create a for loop
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
# however this now produces 0s because some of the agents have been tested 
# against themself which would mean the agent a minus agent a will be 0
# we need to get rid of this. 
        if distance > 0 : 
            print(distance)
# however this is an issue because there may be distances above 0 but
# they can't be included. ANother problem is that agent 1 will be compared to
# agent 2, and vice versa- so we have repeated results. we want to 
# eliminate these repeated results by creating another loop
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = distance_between(agents[x], agents [z])
        print (distance)
