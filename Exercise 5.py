
# coding: utf-8

# In[3]:

def completegraph(n):
    newgraph=[[0 for j in range(n)] for i in range(n)]
    for i in range (0, n):
        for j in range (0,n):
            if i!=j:
                newgraph[i][j]=1
    print(newgraph)

completegraph(4)
                
    
    


# In[5]:

import random
def randomgraph(n):
    newgraph=[[0 for j in range(n)] for i in range(n)]
    for i in range (0, n):
        for j in range (0,n):
            if i!=j:
                newgraph[i][j]=random.randint(0,1)
    for i in range (0, n): #for the undirected graph - to make the matrix symmetric
        for j in range (0,n):
            if newgraph[i][j]==1:
                newgraph[j][i]=1 
    print(newgraph)
    
randomgraph(5)


# In[29]:

import random
def randomgraph(n):
    newgraph=[[0 for j in range(n)] for i in range(n)]
    for i in range (0, n):
        for j in range (0,n):
            if i!=j:
                newgraph[i][j]=random.randint(0,1)
    for i in range (0, n): #for the undirected graph - to make the matrix symmetric
        for j in range (0,n):
            if newgraph[i][j]==1:
                newgraph[j][i]=1 
    return(newgraph)
n=3    
g = randomgraph(n)
print(g)

col=[]
for i in range (0, n):
    col.append(0)
def cyclesearch(v,p):
    col[v]=1 #assign the current vertice the status of visited: "1" means visited
    for i in range (0,n):
        if g[v][i]>0: #if there is an edge assigned to the vertice then we start looking for a cycle
            to=i
            if col[to] == 0: #if the vertice has never been visited, we run the cycle again for non-parent neighbours
                if to!=p: #we want to exclude parent vertices
                    if (cyclesearch(to, v)== True):
                        return True
            elif col[to] == 1: #is the vertice was visited before, we have found a cycle
                if p!=to:
                    return True       
    col[v] = 2
    return False

found=False

for i in range (0, n):
    if (cyclesearch(i,i) == True):
        found = True
        print("Cycle found")
        break

if (found == False):
    print("Cycle not found")
        
    
    

            
            

 
    


# In[ ]:



