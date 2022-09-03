#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            x='-'+x[-1:-len(x):-1]
            if int(x)>-2147483648 and int(x)<2147483647:
                return int(x)
            else:
                return 0
        if int(x[-1: :-1])>-2147483648 and int(x[-1: :-1])<2147483647:
            return int(x[-1: :-1])
        else:
            return 0
        