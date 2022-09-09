#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        if nums[-1]==target:
            return len(nums)-1
        if nums[-1]<target:
            return len(nums)
        if nums[0]>target:
            return 0
        while l<len(nums)-1:
            if nums[l]==target:
                return l
            elif nums[l]<target and nums[l+1]>target:
                    return l+1
            l+=1
        

