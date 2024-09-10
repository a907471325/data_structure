1438. 绝对差不超过限制的最长连续子数组from sortedcontainers import SortedDict
class Solution:
    # brute force n ^ 2 超时
    # def longestSubarray(self, nums: List[int], limit: int) -> int:

    #     d = {nums[0]:1}
    #     res = 1
    #     j = 0

    #     for i in range(1, len(nums)):
    #         x = nums[i]
    #         if x not in d:
    #             d[x] = 0
    #         d[x] += 1
    #         while j < i and d.keys() and abs(x-max(d.keys())) > limit or abs(x-min(d.keys())) > limit:
    #             d[nums[j]] -= 1
    #             if d[nums[j]] == 0:
    #                 d.pop(nums[j])
    #             j += 1

    #         res = max(res, i-j+1)
    #     return res

    # sorted list n * log n
    # def longestSubarray(self, nums: List[int], limit: int) -> int:

    #     d = SortedDict()
    #     d[nums[0]] = 1
    #     res = 1
    #     j = 0

    #     for i in range(1, len(nums)):
    #         x = nums[i]
    #         if x not in d:
    #             d[x] = 0
    #         d[x] += 1
    #         while j < i and abs(d.peekitem(0)[0] - d.peekitem(len(d) - 1)[0]) > limit:
    #             d[nums[j]] -= 1
    #             if d[nums[j]] == 0:
    #                 d.pop(nums[j])
    #             j += 1

    #         res = max(res, i - j + 1)

    #     return res

    # 单调队列 n
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        qmax, qmin = deque(), deque()
        qmax.append(0)
        qmin.append(0)

        res = 1
        j = 0

        for i in range(1, len(nums)):
            while qmax and nums[qmax[-1]] < nums[i]:
                qmax.pop()
            while qmin and nums[qmin[-1]] > nums[i]:
                qmin.pop()

            qmax.append(i)
            qmin.append(i)


            while j < i and abs(nums[qmax[0]] - nums[qmin[0]]) > limit:
                if nums[qmax[0]] == nums[j]:
                    qmax.popleft()
                if nums[qmin[0]] == nums[j]:
                    qmin.popleft()
                j += 1

            res = max(res, i - j + 1)

        return res

