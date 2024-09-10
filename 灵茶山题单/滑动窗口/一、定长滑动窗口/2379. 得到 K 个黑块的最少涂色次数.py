class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_w = 100
        cur = 0

        for i, x in enumerate(blocks):
            if x == "W":
                cur += 1
            if i < k - 1:
                continue
            min_w = min(min_w, cur)

            if blocks[i - k + 1] == "W":
                cur -= 1
        return min_w