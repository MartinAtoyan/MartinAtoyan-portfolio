class Solution:
    def isValid(self, s: str) -> bool:

        di = {"(": ")", "[": "]", "{": "}"}
        ls = []

        for i in s:
            if i in di:
                ls.append(di[i])
            else:
                if not ls or ls.pop() != i:
                    return False

        return len(ls) == 0