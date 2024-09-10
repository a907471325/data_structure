class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        return max(self.helper(answerKey, k, 'T'), self.helper(answerKey, k, 'F'))

    def helper(self, answerKey, k, target):

        other_num = 0
        j = 0
        res = 0
        for i, x in enumerate(answerKey):
            if x != target:
                other_num += 1
            while other_num > k:
                if answerKey[j] != target:
                    other_num -= 1
                j += 1
            res = max(res, i - j + 1)
        return res