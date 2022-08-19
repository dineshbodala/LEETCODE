#Missing Number

#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
 
#Basic sum of n natural numbers formula
class Solution(object):
    def missingNumber(self, nums):
        return (len(nums))*(len(nums)+1)//2 - sum(nums)

#All Testcases passed
class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        
        
        
        
        
         