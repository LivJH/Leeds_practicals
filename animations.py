# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:42:28 2018

@author: gyojh
"""

#### copy and pasted code
import csv 
import agentframework
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 

fig.clear()   
# setting the plotting frame
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#### ENVRONMENT######

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


##########################################################

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20


#this links to the agentframework.py file, which has created a function for this code
a = agentframework.Agent(environment, agents)
a.y
print(a.y, a.x)

#this is another part of the agentframework.py file
a.move()
print(a.y,a.x)




# Create the agents, and put fig clear in so that once the loop is complete it will end
agents = []
fig.clear()
# this creates the agents, put does not plot them 
for k in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    #this is plotting the environment
    matplotlib.pyplot.imshow(environment)
    #this is plotting the agents
    matplotlib.pyplot.scatter(agents[k].x,agents[k].y)
    #this is plotting the axis
    matplotlib.pyplot.xlim(0, 120)
    matplotlib.pyplot.ylim(0, 120)


# animate/update the agents and putting in the environment 
def update(frame_number):
    
    #plotting the environment
    fig.clear()   
    matplotlib.pyplot.imshow(environment)
   
    
    # within the environment- making the agent move/eat by updating the co-ords and we plot them
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        #print(i)
        
        # plotting agents
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.xlim(0, 120)
        matplotlib.pyplot.ylim(0, 120)
        
#    for i in range(num_of_agents):
#        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#        matplotlib.pyplot.xlim(0, 120)
#        matplotlib.pyplot.ylim(0, 120)

        #print(agents[i].x,agents[i].y)

# this allows the agent to move
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()


### there is a problem when this runs, as the environment is not in the background


