# good solution
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
#         for i in range(res):
#             res ^= i
#             res ^= nums[i]
#         return res

# bad solution
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = sum(nums)
#         size = len(nums)
#         sum_ = 0
#         for i in range(size + 1):
#             sum_ += i
#         return sum_ - res