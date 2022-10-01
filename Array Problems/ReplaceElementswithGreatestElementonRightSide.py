#Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#After doing so, return the array.

class Solution(object):
    def replaceElements(self, arr):
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr            
        