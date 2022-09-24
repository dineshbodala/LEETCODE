class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        csum=sum(Arr[:K])
        maxsum=sum(Arr[:K])
        for i in range(len(Arr)-K):
            csum -= Arr[i]
            csum += Arr[i+K]
            maxsum=max(csum,maxsum)
            
        return maxsum