#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Using Sliding Window

class Solution(object):
    def maxProfit(self, prices):
        i, j = 0, 1
        maxp=0
        while j<len(prices):
            if prices[i]<prices[j]:
                maxp=max(maxp, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return maxp
            