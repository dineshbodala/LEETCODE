#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#3 hrs later, Attempt-10000000, all testcases passed.

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        x=collections.defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')]+=1
            x[tuple(count)].append(i)
        return x.values()

#After few hours of brain storming aand youtube references coded an ideal solution
import collections
class Solution(object):
    def groupAnagrams(self, strs):       
        x=collections.defaultdict(list)
        for i in strs:
            if tuple(sorted(i)) in x:
                x[tuple(sorted(i))].append(i)
            else:
                x[tuple(sorted(i))].append(i)
        return x.values() 
        

 