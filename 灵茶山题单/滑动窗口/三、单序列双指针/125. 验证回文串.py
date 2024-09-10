class Solution:

    def clear(self, s):

        if not s:
            return ""
        s_new = ""

        for ch in s.lower():
            if ord(ch) >= ord("a") and ord(ch) <= ord('z'):
                s_new += ch
            elif ord(ch) >= ord("0") and ord(ch) <= ord('9'):
                s_new += ch

        return s_new

    def isPalindrome(self, s: str) -> bool:

        s = self.clear(s)
        i = 0
        j = len(s) - 1
        # 0,6 1,5 2,4

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

