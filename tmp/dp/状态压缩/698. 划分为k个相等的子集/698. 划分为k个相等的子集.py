from typing import List


class Solution:

    k = 0
    k_len = 0
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_len = sum(nums)
        if total_len % k != 0 or n < k:
            return False
        k_len = total_len // k
        self.k = k
        self.k_len = k_len
        memo = [-1] * (1 << n)
        return self.dfs(nums, 0, 0, 0, 0, memo)

    def dfs(self, nums, used, d, cur_len, cur_k, memo):
        if d == len(nums):
            return cur_k == self.k
        elif memo[used] != -1:
            return memo[used] == 1
        else:
            res = False
            for i, val in enumerate(nums):
                if used & 1 << i != 0:
                    continue
                remain = self.k_len - cur_len
                if val <= remain:
                    res = res | self.dfs(nums,
                                         used | 1 << i,
                                         d+1,
                                         0 if val == remain else cur_len + val,
                                         cur_k + 1 if val == remain else cur_k,
                                         memo)
                if res:
                    break
            memo[used] = 1 if res else 0
            return res






if __name__ == '__main__':
    so = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(so.canPartitionKSubsets(nums, k))





