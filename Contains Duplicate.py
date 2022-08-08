#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        x={}
        for i in nums:
            if i not in x:
                x[i]=1
            else:
                return True
        return False