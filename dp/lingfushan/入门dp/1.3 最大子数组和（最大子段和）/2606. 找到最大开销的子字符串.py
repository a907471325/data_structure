import string
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        letters = string.ascii_lowercase
        val_dict = {}
        for index, letter in enumerate(letters):
            val_dict[letter] = ord(letter) - 96

        for index, ch in enumerate(list(chars)):
            val_dict[ch] = vals[index]

        nums = []
        for ch in s:
            nums.append(val_dict[ch])

        cur, pre = 0, 0
        res = 0
        for i in range(len(nums)):
            pre = cur
            cur = max(pre + nums[i], nums[i])
            res = max(cur, res)
        return max(0, res)

