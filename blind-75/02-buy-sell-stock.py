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
