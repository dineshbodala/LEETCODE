#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=0
        if len(s)==1:
            return 1
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                x+=1
            elif x>0:
                break
        return x
            
                
        