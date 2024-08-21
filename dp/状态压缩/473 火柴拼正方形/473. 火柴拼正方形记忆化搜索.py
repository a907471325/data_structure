class Solution:
    width = 0

    def makesquare(self, matchsticks) -> bool:
        perimeter = sum(matchsticks)
        width = perimeter // 4
        print(width)
        if perimeter % 4 != 0 or len(matchsticks) < 4 or max(matchsticks) > width:
            return False

        self.width = width
        # 1111 222 333 5
        # 123 123 123 15
        memo = [0 for i in range(1 << len(matchsticks))]
        return self.dfs(matchsticks, 0, 0, width, 4, memo)

    def dfs(self, nums, used, d, remain_one_side_len, remain_matches_side_num, memo):
        # print("used: " + str(used))

        if d == len(nums):
            # print("used: " + str(used))
            # print("remain_one_side_len: " + str(remain_one_side_len))
            # print("remain_matches_side_num: " + str(remain_matches_side_num))
            # print("#")
            if remain_matches_side_num == 0:
                return True
            return False
        elif memo[used] != 0:
            return memo[used] == 1
        else:
            res = False
            for i in range(len(nums)):
                if used & 1 << i != 0:
                    continue
                if remain_one_side_len - nums[i] < 0:
                    continue

                if remain_one_side_len - nums[i] == 0:
                    remain_one_side_len_next = self.width
                    remain_matches_side_num_next = remain_matches_side_num - 1
                else:
                    remain_one_side_len_next = remain_one_side_len - nums[i]
                    remain_matches_side_num_next = remain_matches_side_num
                res |= self.dfs(nums,
                                used | 1 << i,
                                d + 1,
                                remain_one_side_len_next,
                                remain_matches_side_num_next,
                                memo)
                if res:
                    break
            memo[used] = 1 if res else -1
            return res


if __name__ == '__main__':
    # matchsticks = [2, 2, 2, 2]
    # matchsticks = [1, 1, 2, 2, 2]
    # matchsticks = [3, 3, 3, 3, 4]
    # matchsticks = [1, 2, 1, 2, 1, 2, 1, 2]
    matchsticks = [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
    so = Solution()
    res = so.makesquare(matchsticks)
    print(res)
    pass
