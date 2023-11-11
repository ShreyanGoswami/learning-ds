class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        for i, p in enumerate(prices):
            while s and prices[s[-1]] >= p:
                j = s.pop()
                prices[j] -= p
            s.append(i)
        return prices 
