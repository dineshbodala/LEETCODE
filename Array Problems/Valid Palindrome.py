#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r=l+1, r-1
        return True
        
    def alphanum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')) 
 
#own solution
 class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        Strarr=[chr(i) for i in range(ord('a'), ord('z')+1)]
        for i in range(0,10):
            Strarr.append(str(i))
        newstr=''
        for i in s:
            if i in Strarr:
                newstr+=i
        if newstr==newstr[-1::-1]:
            return True
        return False
        
        