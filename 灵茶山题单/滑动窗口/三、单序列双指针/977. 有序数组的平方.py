class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = []
        n = len(nums)
        i=0
        j=n-1
        while i < j:
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]
            if left <= right:
                q.insert(0, right)
                j -= 1
            else:
                q.insert(0, left)
                i += 1
        q.insert(0, nums[i] * nums[i])
        return q
