#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#Return the max sliding window.

#Bruteforce sol
class Solution:

    def max_of_subarrays(self,arr,n,k):
        result=[]
        for i in range(n-k+1):
            for j in range(i,i+k):
                result.append(max(arr[i:i+k]))
                break
        return result
        
        
        


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums)==1:
            return [nums[0]]
        if k==1:
            return nums
        maxnum=max(nums[0:k+1])
        maxarr=[]
        maxarr.append(maxnum)
        for i in range(len(nums)-k):
            if maxnum < nums[i+k]:
                maxnum=nums[i+k]
                maxarr.append(nums[i+k])
            else:
                maxarr.append(maxnum)
                
        return maxarr
                
            
        
 #7/271 passed       
class Solution:
    def max_of_subarrays(self,arr,n,k):
        i=0
        j=0
        cmax=-9999
        result=[]
        while j<n:
            if cmax<arr[j]:
                cmax=arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                result.append(cmax)
                j+=1
                i+=1
        return result
            
        
        
        