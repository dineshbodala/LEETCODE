#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        x=int(n/2)
        e=(nums[x-1]+nums[x])/2
        if n%2==0:
            return e
        else:
            return nums[x]
        