#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        else:
            maximum = -sys.maxsize - 1
            sum = 0
            for i in range(len(nums)):
                sum += nums[i]
                if sum > maximum:
                    maximum = sum
                if sum < 0:
                    sum = 0
            return maximum
            
        