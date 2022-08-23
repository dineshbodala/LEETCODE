#Duplicate Number
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x={}
        for  i in nums:
            if i not in x:
                x[i]=1
            else:
                return True
        return False 

# Valid Anagram
#Approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return 1
        else:
            return 0


#Approach 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x, y={}, {}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        
        for i in t:
            if i not in y:
                y[i]=1
            else:
                y[i]+=1
        
        for i in x:
            if i not in y:
                return False
            if x[i]!=y[i]:
                return False 
        return True


#Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            if target-nums[i] in x:
                return i, x[target-nums[i]]
            x[nums[i]]=i




#Group Anagrams
#Approach 1
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=collections.defaultdict(list)
        for i in strs:
            if tuple(sorted(i)) not in x:
                x[tuple(sorted(i))]
                
        for i in strs:
            if tuple(sorted(i)) in x:
                x[tuple(sorted(i))].append(i)
                
        return x.values()

#Product of Array Except Self
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        x=[]
        for i in range(len(nums)):
            x.append(pre)
            pre=pre*nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            x[i]=x[i]*post
            post=post*nums[i]
            
        return x


            
            