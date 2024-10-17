class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        sum = 0
        res = []
        for i in digits:
            sum = sum * 10 + i
        sum += 1
        sum = str(sum)
        for i in range(len(sum)):
            res.append(int(sum[i]))

        return res
