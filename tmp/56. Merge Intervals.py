from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        points = []
        for interval in intervals:
            points.append([interval[0], -1])
            points.append([interval[1], 1])
        points = sorted(points, key=lambda a:(a[0], a[1]))

        ans = []
        left_most, right_most = 1e9, 0
        count = 0
        for p in points:
            if p[1] == -1:
                left_most = min(left_most, p[0])
                count += 1
            if p[1] == 1:
                right_most = max(right_most, p[0])
                count -= 1
                if count == 0:
                    ans.append([left_most, right_most])
                    left_most, right_most = 1e9, 0
        return ans

