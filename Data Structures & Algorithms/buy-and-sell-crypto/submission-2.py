class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         profit = sell - buy
        #         max_profit = max(max_profit, profit)
        
        # return max_profit



        # Real Solution
        left = 0 
        right = 1
        max_profit = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            if sell > buy: 
                profit = sell - buy
                max_profit = max(max_profit, profit)
                right += 1
            else:
                left = right # cheaper time to buy so we move the buy time to left
                right += 1
            
        return max_profit

