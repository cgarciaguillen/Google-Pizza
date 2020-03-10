

def Pizza(M,N,S):
    if M>=sum(S):
        K=N
        L=S
        return (K,L)
    
    else:
        for i in range(len(S)):#Numero de pizzas
            for j in S: #1 pizza
                if j==M:
                    K=1
                    L=[S.index(j)]
                    return(K,L)
                
 



M=6 #Max slices
N=4 #Max pizzas
S = [2, 5, 6, 8] #Slices per pizza
           
print(Pizza(M,N,S))              
                
            

#print("K=",K)
#print("L=",L)