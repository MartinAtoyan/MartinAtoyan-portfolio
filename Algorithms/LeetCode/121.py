# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_prof = 0
#
#         buy = prices[0]
#         for i in prices[1:]:
#             if buy - i > 0:
#                 buy = i
#
#             max_prof = max(max_prof, i - buy)
#
#         return max_prof