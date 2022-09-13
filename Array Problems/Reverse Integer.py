#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[-1::-1]:
            return True
        else:
            return False

#method 2
n=12
r=0
y=0
while n>0:
    y=n%10
    r=r*10+y
    n=n//10
print(r)
        
        
