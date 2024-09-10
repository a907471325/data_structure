class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # a = "ulacfd", b = "jizalu"
        # a = "ulacfd", b = "jizalu"

        def is_palin(s):
            n = len(s)
            l = 0
            r = n - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if is_palin(a) or is_palin(b):
            return True

        def check(s1, s2):
            n = len(s1)
            l = 0
            r = n - 1
            while l <= r:
                if s1[l] != s2[r]:
                    break
                l += 1
                r -= 1
            if l > r:
                return True
            else:
                return is_palin(s1[l:r + 1]) or is_palin(s2[l:r + 1])

        return check(a, b) or check(b, a)




