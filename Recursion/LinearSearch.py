def linearsearch(x,i):
    if len(x)==0:
        return False
    if x[0]==i:
        return True
    else:
        return linearsearch(x[1:],i)


x=[1,2,3,4,5]
i=7
print(linearsearch(x,i))