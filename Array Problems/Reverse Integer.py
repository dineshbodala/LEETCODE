#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[-1::-1]:
            return True
        else:
            return False
        
        
