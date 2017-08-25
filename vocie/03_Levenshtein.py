#!python3
def analysis(list1,list2):
    if type(list1)!=type([]):
        list(list1)
        list(list2)
        
    m=len(list1)
    n=len(list2)

    v0=list(range(m+1))
    v1=list(range(m+1))
    v1[0]=0

    if m==0 or n==0:
        print('list is empty')
        return(0)
    else:
        for j in range(n):
            v1[0]=v1[0]+1
            for i in range(m):
                if str(list1[i])==str(list2[j]):
                    cost=0
                else:
                    cost=1
                
                v1[i+1]=min(v1[i]+1,v0[i+1]+1,v0[i]+cost)

            for nn in range(m+1):
                v0[nn]=v1[nn]
        result=1-v1[-1]/max(m,n)
        print(result)
        return(result)
analysis('stecai1','stecai2')
