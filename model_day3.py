# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:10:17 2018

@author: gyojh
"""



### this part of the prac involves getting the agents and their code from the
### agentframework.py file and using it to move the agents


import random
import operator
import matplotlib.pyplot
#this has been added for this practical
import agentframework



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


#this links to the agentframework.py file, which has created a function for this code
a = agentframework.Agent(environment, agents)
a.y
print(a.y)
print(a.x)
#this is another part of the agentframework.py file
a.move()
print(a.y,a.x)


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents)

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()



