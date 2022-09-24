#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#Return the max sliding window.

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
                
            
        
        
        