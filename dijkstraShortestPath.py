#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pandas will be used to import data from excel sheet
import pandas as pd

#graph implementation, acacency list
def add_vertex(v):
    #global varibles from the driver function use to create a graph of connection between cities
    global cityWGraph   #2d list
    global vertices_no  #integer counter
    global vertices     #list of vertices added
    
    #do nothing if the vertices already exists in the list of vertices
    if v in vertices:
        print()
    #process of adding the input vertex to list
    else:
        vertives_no = vertices_no + 1   #increment counter
        vertices.append(v)              #append vertices
        if vertices_no > 1:             
            for vertex in cityWGraph:   #graph initialization
                vertex.append(0)
        temp = []                        
        for i in range(vertices_no):
            temp.append(0)
        cityWGraph.append(temp)

def add_edge(v1, v2, e):
    #same global variables as in previous function
    global cityWGraph
    global vertices_no
    global vertices
    
    if v1 not in vertices:
        print()
    elif v2 not in vertices:
        print()
    else:
        index1 = vertices.index(v1) #find index of v1
        index2 = vertices.index(v2) #find indesx of v2
        cityWGraph[index1][index2] = e  #using the adjacency list, assign the edge


# In[4]:


#utility functions that are used to convert values from excel sheet into desired values 
def convertName(s1): #accepts name
        global names
        x = 0
        for i in names:
            x += 1
            if i == s1:
                return x #outputs coresponding index
        print("This city is not avalible.")
        return   

def convertToName(idx): #accepts index
    global names
    return names[idx-1] #returns string name of coresponding city


# In[5]:


from collections import defaultdict
class Graph:
    #function that finds the minimum distance
    def minDistance(self,dist,queue):
        minimum = float("Inf")       #initialize minimun as infinite to use for comparision
        min_index = -1               #initizalize minimun index
         
        for i in range(len(dist)): #loop through the vertecies
            if dist[i] < minimum and i in queue: #finding minimum distance from dist array
                minimum = dist[i]
                min_index = i
        return min_index
    
    #recursive printing function for paths
    def printPath(self, currentPath, j): 
        if currentPath[j] == -1 :
            print(convertToName(j),end="    ")
            return
        self.printPath(currentPath , currentPath[j])
        print (convertToName(j),end="   ")
         
    #dijkrsta's algorithm implementaion with graph
    def shortestPath(self, graph, src, dest):
        #initialization of row and col varibles that will be used later
        row = len(graph)
        col = len(graph[0])
 
        #dist is an array used to hold the shortest distance from the source
        #city to the destination
        dist = [float("Inf")] * row # Initialize all distances as INFINITE
 
        #intialize variable to hold the current shortest path
        currentPath = [-1] * row
        
        #initialze distance from first city
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []              #initialize queue
        for i in range(row):    #loop through the row
            queue.append(i)     #add the varibles
        
        while queue:
            #u is the closest vertex in queue
            j = self.minDistance(dist,queue)
            if( j == -1):    #error prevention
                break
            queue.remove(j)   #remove the closest in queue
    
           #if valid conditions are meet, we will distribute
            for i in range(col):
                if graph[j][i] and i in queue:           #if the vertex is in the queue and there exists an edge between u and i
                    if dist[j] + graph[j][i] < dist[i]:  #is the new weight smaller than the current value for distance
                        dist[i] = dist[j] + graph[j][i]  #add this vertex into the distance counter
                        currentPath[i] = j              #add this vertex to the current shortest path

        #printing of solution
        print("Vertex \t\t\t\tDistance from Source\t\t Path")
        print("\n%s --> %s \t\t%d \t\t\t\t" % (convertToName(src), convertToName(dest), dist[dest]),end=" ")
        self.printPath(currentPath,dest)


# In[6]:


#driver code

#global varibles that we use to create the weighted graph of cities
vertices = []
vertices_no = 0
cityWGraph = [[0]*107 for i in range(107)]

#using pandas, import the values stored in the sheet
graphdata = pd.read_excel("convertedGraphData.xlsx")
src = graphdata['src'].values.tolist()
dest = graphdata['dest'].values.tolist()
miles = graphdata['miles'].values.tolist()

#list of city names
stringdata = pd.read_excel("cityKeys.xlsx")
names = stringdata['name'].values.tolist()

#creating graph
#adding vertieces
count = 0
while (count < len(src)):
    add_vertex(src[count])
    count += 1

#adding edges
count = 0
while (count < len(src)):
    add_edge(src[count], dest[count], miles[count])
    count += 1

#g is the graph object that we are using to call our function
g = Graph()

###########################################################################################################
################ < USER > < ENTER THE NAMES OF YOUR CITIES INTO THE VARIBLE NAMES BELOW > #################
###########################################################################################################
START_CITY = "Sacramento"
DESTINATION = "Mt. Shasta"

#function call to find shortest path
g.shortestPath(cityWGraph, convertName(START_CITY), convertName(DESTINATION))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




