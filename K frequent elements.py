#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



#Attempt-1 7/27 testcases Passed

class Solution(object):
    def topKFrequent(self, nums, k):
        m1, m2=0,0
        n1,n2=0,0
        if len(nums)==1:
            return [nums[0]]
        elif len(nums)==2 and nums[0]==nums[1]:
            return [nums[0]]
        elif len(nums)==2:
            return [nums[0], nums[1]]
        else:
            x={}
            for i  in nums:
                if i not in x:
                    x[i]=1
                else:
                    x[i]+=1
        y=sorted([x[i] for i in x])
        m1,m2=y[-1], y[-2]
        for i in nums:
            if nums.count(i)==m1:
                n1=i
            elif nums.count(i)==m2:
                n2=i
        return n1,n2
                
            