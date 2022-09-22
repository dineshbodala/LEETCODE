#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#Note:
#Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type.
# It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

#First Attempt
class Solution(object):
    def hammingWeight(self, n):
        n=str(n)
        if len(n)==0:
            return 0
        elif n[0]=='1':
            return 1+self.hammingWeight(n[1:])
        elif n[0]=='0':
            self.hammingWeight(n[1:])

        

 