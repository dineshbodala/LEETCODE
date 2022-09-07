x=[]
for i in input1:
    x.append(ord(i))
n=[1]*len(x)
for i in range(1,len(x)):
    for j in range(0,i):
        if x[i]>x[j] and n[i]<n[j]+1:
            n[i]=n[j]+1
maxc=0
for i in range(len(x)):
    maxc=max(maxc, n[i])
return maxc
