class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strNum = str(num)
        c = 0
        for i in range(k, len(strNum)+1):
            d = int(strNum[i-k : i])
            if d != 0 and num% d == 0:
                c += 1
        return c