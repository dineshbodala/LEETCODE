#To find out frequency of elements in an array using dict

x={}
n=[1,2,3,4,5]
for i in n:
    x[i]=1+x.get(i,0)


    