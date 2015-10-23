
# coding: utf-8



import random
def randomgraph(n):
    newgraph=[[0 for j in range(n)] for i in range(n)]
    for i in range (0, n):
        for j in range (0,n):
            if i!=j:
                newgraph[i][j]=random.randint(0,n)
    for i in range (0, n): #for the undirected graph - to make the matrix symmetric
        for j in range (0,n):
            if newgraph[i][j]!=0:
                newgraph[j][i]=newgraph[i][j] 
    return(newgraph)
n=5
g = randomgraph(n)
print(g)





