import string


import string
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        az = string.ascii_lowercase
        d = {ch:i+1 for i, ch in enumerate(az)}
        nums = [d[_] for _ in s]
        last = power ** k % modulo
        cur_sum = 0
        ans = 0
        n = len(nums)
        for i in range(n-1, n-k-1, -1):
            cur_sum = (cur_sum * power + nums[i]) % modulo

        if cur_sum == hashValue:
            ans = n-k

        for i in range(n-k-1, -1, -1):
            cur_sum = (cur_sum * power + nums[i] - nums[i+k] * last) % modulo

            # t = cur_sum % modulo
            if cur_sum == hashValue:
                ans = i
        return s[ans:ans+k]


if __name__ == '__main__':
    s = "fbxzaad"
    power = 31
    modulo = 100
    k = 3
    hashValue = 32
    # s = "fbxzaad"
    so = Solution()
    print(so.subStrHash(s, power, modulo, k, hashValue))

