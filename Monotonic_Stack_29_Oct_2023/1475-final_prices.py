class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        for i, p in enumerate(prices):
            while s and prices[s[-1]] >= p:
                j = s.pop()
                prices[j] -= p
            s.append(i)
        return prices 
    
# class Solution:
#     def __init__(self):
#         self.stack = []

#     def peek(self):
#         return self.stack[-1]

#     def pop(self):
#         return self.stack.pop()

#     def push(self, i):
#         self.stack.append(i)

#     def finalPrices(self, prices: List[int]) -> List[int]:
#         for i, price in enumerate(prices):
#             while self.stack and prices[self.peek()] >= price:
#                 idx = self.pop()
#                 prices[idx] -= price
#             self.push(i)
#         return prices