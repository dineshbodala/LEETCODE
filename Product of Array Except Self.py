#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        pre=1
        post=1
        x=[]
        for i in nums:
            x.append(pre)
            pre=pre *  i
        
        for i in range(len(nums)-1,-1,-1):
            x[i]=post * x[i]
            post=post*nums[i]
      
        return x
        
