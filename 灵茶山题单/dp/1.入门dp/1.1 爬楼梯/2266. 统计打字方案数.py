MOD = 10 ** 9 + 7
ldict = {2:3, 3:3, 4:3, 5:3, 6:3, 7:4, 8:3, 9:4}
seqdict = {}
for k,v in ldict.items():
    skey = str(k)
    seqdict[skey] = []
    for _ in range(1, v+1):
        seqdict[skey].append(skey * _)

class Solution:
    # dfs
    def countTexts(self, pressedKeys: str) -> int:

        cache = [-1] * (len(pressedKeys) + 1)
        def dfs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if cache[n] != -1:
                return cache[n]
            s = pressedKeys[n-1]
            res = 0
            for i in seqdict[s]:
                if pressedKeys[n-len(i):n] == i:
                    res = res + dfs(n-len(i))
                    res = res % MOD
            cache[n] = res
            return res

        ans = dfs(len(pressedKeys))
        return ans

    # dp
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        f = [0] * (n + 1)
        f[0] = 1

        for i in range(1, n + 1):
            s = pressedKeys[i-1]
            for seq in seqdict[s]:
                if i-len(seq) >= 0 and pressedKeys[i-len(seq):i] == seq:
                    f[i] += f[i-len(seq)]
                    f[i] = f[i] % MOD
        return f[n]


if __name__ == '__main__':
    so = Solution()
    pressedKeys = "222222222222222222222222222222222222"
    s = so.countTexts(pressedKeys)
    print(s)
