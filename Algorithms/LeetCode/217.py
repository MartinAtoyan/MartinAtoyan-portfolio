# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         size = len(nums)
#         di = {}
#         for i in range(size):
#             if nums[i] in di:
#                 di[nums[i]] += 1
#             else:
#                 di[nums[i]] = 1
#
#         for i in di.values():
#             if i >= 2:
#                 return True
#         return False



