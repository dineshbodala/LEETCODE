#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.

#3/71 passed
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        x=max(nums)+1
        y=[1]*x
        c=1
        maxc=-9999
        for i in nums:
            y[i]=0
        for i in range(len(y)-1):
            if y[i]==y[i+1]==0:
                c+=1
            else:
                maxc=max(c,maxc)
        return max(c,maxc)
            
            