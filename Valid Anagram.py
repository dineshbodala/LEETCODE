#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Attempt 1 passed 27/37 cases
class Solution(object):
    def isAnagram(self, s, t):
        x, y=0,0
        for i in s:
            x+=ord(i)
        for i in t:
            y+=ord(i)
        
        if x==y:
            return True
        return False

#Attempt 4-All testcases passed. Bad TC and SC
def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        for i in s:
            if s.count(i)!=t.count(i):
                return False
            if i not in t:
                return False
        return True

#Attempt 6- All test cases passed
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        x,y={}, {}
        for  i in s:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        for  i in t:
            if i not in y:
                y[i]=1
            else:
                y[i]+=1
                
        for i in x:
            if i not  in y:
                return False
            if x[i] != y[i]:
                return False
        return True


