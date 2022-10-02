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


#All Passed
#Burra Vaadali Guru
def printFirstNegativeInteger(arr, n, k):
    i=0
    j=0
    negarr=[]
    result=[]
    while j<n:
        if arr[j]<0:
            negarr.append(arr[j])
        
        if j-i+1 < k:
            j+=1
            
        elif j-i+1==k:
            if len(negarr)==0:
                result.append(0)
            else:
                result.append(negarr[0])
                if arr[i]==negarr[0]:
                    negarr.pop(0)
            i+=1
            j+=1
    return result
                
                