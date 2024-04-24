class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        if n < 3:
            return 0
        for i in range((n-3)+1):
            substring = s[i:i+3]
            substring_set = set(substring)
            if len(substring_set) == 3:
                c += 1
        return c