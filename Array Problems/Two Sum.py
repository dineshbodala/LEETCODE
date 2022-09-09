#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Attempt 1, 47/57 testcases passed
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums:
                return i, nums.index(target-nums[i])

#Attempt 2 49/57 testcases passed
class Solution(object):
    def twoSum(self, nums, target):
        x={}
        for i in range(len(nums)):
            if nums[i] not  in x:
                x[nums[i]]=i
        for i in x:
            if target-i in x:
                return x[i], x[target-i]
            

#All test cases pased
class Solution(object):
    def twoSum(self, nums, target):
        x={}
        for i in range(len(nums)):
            if target-nums[i] in x:
                return i, x[target-nums[i]]
            x[nums[i]]=i
            
       