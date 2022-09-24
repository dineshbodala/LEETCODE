class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        c=0
        maxc=-9999
        ind=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in s[i:j]:
                    c+=1
                else:
                    maxc=max(c,maxc)
                    c=0
                    break
        return maxc
                
            