class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0

        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         max_profit = max(max_profit, sell - buy)

        # return max_profit


        
        # Real Solution
        max_profit = 0
        left = 0 
        right = 1

        while right < len(prices):  # goes from left to right 
            buy = prices[left]
            sell = prices[right]

            if sell > buy:  # if the current window is valid we calc the profit
                max_profit = max(max_profit, sell - buy)
                right += 1
            else:   # if the sell price is less than the buy price we found a new lower price to buy at so update pointer
                left = right 
                right += 1
        
        return max_profit