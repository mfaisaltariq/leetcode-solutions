'''
https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=2
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List
def maxProfit( prices: List[int]) -> int:
    max_profit = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

print(maxProfit([7,1,5,3,6,4]))
