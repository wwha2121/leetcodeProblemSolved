from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currentMaxProfit = 0
        if len(prices) == 1:
            return currentMaxProfit
        elif len(prices) == 2:
            if prices[-2] < prices[-1]:
                return prices[-1] - prices[-2]
            elif prices[-2] >= prices[-1]:
                return currentMaxProfit

        currentMaxProfit = prices[-1] - prices[-2]
        maxNumber = max(prices[-2], prices[-1])

        for number in prices[-3::-1]:
            maxNumber = max(maxNumber, number)
            currentMaxProfit = max(maxNumber - number, currentMaxProfit)

        if currentMaxProfit < 0:
            return 0

        return currentMaxProfit

        ##일단 완전탐색알고리즘풀어보고 변형해서 다이나믹으로 ...



solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))