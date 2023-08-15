class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        #ideally, maximize the profit of a transaction

        #this method works but is O(n^2) time complexity because of the two loops
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
        """

        #by using left and right pointers, we can do a simplified version of what is happening above
        left = 0 #buy
        right = 1 #sell
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left] #the current profit possible
            if prices[left] < prices[right]: #as long as the left value is lower that the right
                max_profit = max(current_profit, max_profit) #assign max_profit to the hightest value between the two
            else:
                left = right #increment the left pointer since there is still a lower value available at the next index
            right += 1 #move right an index over to start the process over again
        return max_profit