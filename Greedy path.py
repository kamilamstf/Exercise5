
    
import random
def randomgraph(n):
    newgraph=[[0 for j in range(n)] for i in range(n)]
    for i in range (0, n):
        for j in range (0,n):
            if i!=j:
                newgraph[i][j]=random.randint(0,n)
    for i in range (0, n): 
        for j in range (0,n):
            if newgraph[i][j]==1:
                newgraph[j][i]=1 
    return newgraph

n=8
col=[]

for i in range (0, n): 
    col.append(0)

def greedysearch(a, b): 
    current = a
    col[a]=1 
    visited=[]

    while current != b:
        min = 1000
        to = -1
        for i in range (0,n):
            if g[current][i]>0:
                if g[current][i] < min and not col[i] == 1:
                    min = g[current][i]
                    to = i
        if to == -1:
            if len(visited)==0:
                return False
            else:
                current=visited.pop()
            
        else:
            visited.append(current)
            current=to
            col[current]=1
    visited.append(b)
    print(visited)
                    
g = randomgraph(8)
print(g) 
greedysearch(0, 3)
