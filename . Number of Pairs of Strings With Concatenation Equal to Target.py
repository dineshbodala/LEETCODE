#. Number of Pairs of Strings With Concatenation Equal to Target
#Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) 
#such that the concatenation of nums[i] + nums[j] equals target

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    c+=1
        return c
        
        
        