MOD = 10 ** 9 + 7


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        n = len(arr)
        res = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1

            if sum(arr[i:i + 3]) > target:
                break
            if arr[i] + arr[-1] + arr[-2] < target:
                continue

            while l < r:
                sum1 = arr[i] + arr[l] + arr[r]
                if sum1 > target:
                    r -= 1
                elif sum1 < target:
                    l += 1
                else:
                    if arr[l] == arr[r]:
                        res += (r - l) * (r - l + 1) // 2
                        break

                    lnum = rnum = 1
                    l += 1
                    while arr[l] == arr[l - 1]:
                        l += 1
                        lnum += 1

                    r -= 1
                    while arr[r] == arr[r + 1]:
                        r -= 1
                        rnum += 1
                    res += lnum * rnum
        return res % MOD

