def revarr(x,i,j):
    if i>=j:
        return x
    x[i],x[j]=x[j],x[i]
    return revarr(x,i+1,j-1)

x=[1,2,3,4]
i=0
j=len(x)-1
print(revarr(x,i,j))