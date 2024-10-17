class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] >= nums[j]:
                    nums[i] ^= nums[j]
                    nums[j] ^= nums[i]
                    nums[i] ^= nums[j]


