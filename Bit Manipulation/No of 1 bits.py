class Solution(object):
    def hammingWeight(self, n):
        cnt=0
        while n:
            if n%2==1:
                cnt+=1
            n = n >> 1
        return cnt
                
            
        