def smallworld(N,K, b):
    edges=0
    import random
    smw=[[0 for j in range(N)] for i in range(N)]
    while (edges <(K*N)):
        for i in range(0,N):
            for j in range(0,N):
                    if abs(i-j)%(N-1-K/2)>0 and abs(i-j)%(N-1-K/2)<(K/2):
                        smw[i][j]=1
                        if smw[i][j]==1:
                            smw[j][i]=1
        for i in range(0,N):
            for j in range(0,N):
                if smw[i][j]==1:
                    edges = edges + 1
                        
    for i in range(0,N):
                print(smw[i])
    print("Adjacency matrix for small-world network after rewiring with probability beta")
    for i in range(0,N):
        for j in range(i,N):
            if smw[i][j]==1:
                if random.random()<=b:
                    smw[i][j]=0
                    smw[j][i]=0
                    newv=i
                    while newv==i:
                        newv=random.randint(0,N-1)
                    smw[i][newv]=1
                    smw[newv][i]=1
                    
    for i in range(0,N):
                print(smw[i])           
                
                    
smallworld(10,4,0.4)
