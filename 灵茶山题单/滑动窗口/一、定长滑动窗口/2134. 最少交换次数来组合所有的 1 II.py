class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 数组中1的数量为k
        # 相当于找所有长为k的字串中，0最少为几个/最多能包含多少个1
        d = Counter(nums)
        k = d[1]
        if k == 1:
            return 0

        s = res = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]
            res = max(res, s)

        for i in range(k-1):
            s += nums[i]
            s -= nums[len(nums)-k+i]
            res = max(res, s)
        return k - res

