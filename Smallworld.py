
def smallworld(N,K):
    import random
    smw=[[0 for j in range(N)] for i in range(N)]
    while (nodes <= (K*2)):
        for i in range(0,N):
	    for j in range(0,N):
	        if abs(i-j)%(N-1-K/2)>0 and abs(i-j)%(N-1-K/2)<(K/2):
                    smw[i][j]=random.randint(0,1)
                    if smw[i][j]==1:
		        nodes = nodes + 1
                        smw[j][i]=1
    print(smw)
                    
smallworld(10,4)
