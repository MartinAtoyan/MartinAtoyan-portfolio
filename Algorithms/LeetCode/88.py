class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        max_size = m + n
        for i in range(n):
            nums1[m + i] = nums2[i]

        for i in range(max_size):
            for j in range(i + 1, max_size):
                if nums1[i] >= nums1[j]:
                    nums1[i] ^= nums1[j]
                    nums1[j] ^= nums1[i]
                    nums1[i] ^= nums1[j]


