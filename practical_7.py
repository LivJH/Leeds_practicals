# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:41:46 2018

@author: gyojh
"""

import csv 
import agentframework
import matplotlib.pyplot
import random

environment = []


#open the file
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# we need a list of rows
for row in reader:
    rowlist = []
# we need to create a value (letter) within a row to put the row (line) within the 
# environment (paper),so we complete this within that order. 
    for value in row:
        rowlist.append(value)  
    environment.append(rowlist)
# we want to see what the environment looks liek 
print(environment)
# to close the file
f.close()




#####  import agent data from the previous practical (model_day3.py) this is
##### so we can make thr agent interact in their environment. 
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


#this links to the agentframework.py file, which has created a function for this code
a = agentframework.Agent(environment, agents)
a.y
print(a.y, a.x)

#this is another part of the agentframework.py file
a.move()
print(a.y,a.x)


## delete this
#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + 
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5




# Make the agent, and add them to the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#add in the code needed for working out distances between agents 
# (last part of prac 6)
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
# working out the distance between two points for when they move around eachother
        distance = agents[x].distance_between(agents[z])
        print (distance)
        

        
# plot the agents living in the environment, the top two lines will 
# zoom into the area where the agents can be found in the environment. 
matplotlib.pyplot.xlim(0, 120)
matplotlib.pyplot.ylim(0, 120)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
