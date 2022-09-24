#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

 #47/52 passed
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        idict=collections.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in idict:
                idict[nums[i]].append(i)
            else:
                idict[nums[i]].append(i)
                
        for i in idict:
            if len(idict[i])>1:
                for j in range(len(idict[i])):
                    for l in range(j,len(idict[i])):
                        if abs(idict[i][j]-idict[i][l])<=k:
                            return True
        
        return False    
                
            
        