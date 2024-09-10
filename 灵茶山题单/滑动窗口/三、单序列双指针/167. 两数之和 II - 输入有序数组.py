class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return []
        n = len(numbers)
        i = 0
        j = n - 1
        res = 0
        while i < j:
            left = numbers[i]
            right = numbers[j]
            res = numbers[i] + numbers[j]
            if res > target:
                j -= 1
            elif res < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return []

