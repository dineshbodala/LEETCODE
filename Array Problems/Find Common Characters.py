#Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
#You may return the answer in any order.

import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x=collections.defaultdict(list)
        y=[]
        for i in words:
            for j in set(i):
                freq=i.count(j)
                if j in x:
                    x[j].append(freq)
                else:
                    x[j].append(freq)
                
        l=len(words)
        c=0
        for i in x:
            if len(x[i])==l:
                c=min(x[i])
                for j in range(c):
                    y.append(i)
        return y
                
                