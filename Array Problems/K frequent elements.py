#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#Attempt-1 7/21 testcases Passed
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

#Attempt-2 7/21 testcases Passed 
class Solution(object):
    def topKFrequent(self, nums, k):
        m1, m2=0,0
        if len(nums)==1:
            return [nums[0]]
        elif len(nums)==2 and nums[0]==nums[1]:
            return [nums[0]]
        elif len(nums)==2:
            return [nums[0], nums[1]]
        else:
            x=[]
            for i in nums:
                x.append(nums.count(i))
            x=sorted(list(set(x)))
            for i in nums:
                if nums.count(i)==x[-1]:
                    m1=i
                elif nums.count(i)==x[-2]:
                    m2=i
            return [m1,m2]

#Attempt-5 All testcases passed
class Solution(object):
    def topKFrequent(self, nums, k):
        x={}
        count=[[] for i in range(len(nums)+1)]
        for i in nums:
            x[i]=1+x.get(i,0)
        for n,c in x.items():
            count[c].append(n)
        sol=[]
        for i in range(len(count)-1, 0, -1):
            for c in count[i]:
                sol.append(c)
            if len(sol)==k:
                return sol
        

#Attempt 6 All testcases passed
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        y=[]
        z=[]
        for i in nums:
                x[i]=1+x.get(i,0)
        for i in x:
            y.append(x[i])
        y.sort()
        y=y[-1:-k-1:-1]
        for i in x:
            if x[i] in y:
                z.append(i)
        return z
            
            
                