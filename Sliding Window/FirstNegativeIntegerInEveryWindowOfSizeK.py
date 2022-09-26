#Given an array A[] of size N and a positive integer K, 
# find the first negative integer for each and every window(contiguous subarray) of size K.

#10050 passed out of 10100
def printFirstNegativeInteger( A, N, K):
    x=0
    negarr=[]
    c=0
    for i in range(len(A)-K+1):
        for j in range(i,i+K):
            if A[j]<0:
                negarr.append(A[j])
                c+=1
                break
        if i+1>len(negarr):
            negarr.append(0)
    return negarr 

