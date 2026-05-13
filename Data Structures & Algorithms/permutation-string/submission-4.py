class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l = 0
        win = len(s1)
        r = l + win
        while r <= len(s2):
            # print(s1,sorted(s2[l:r]), s1 == sorted(s2[l:r]))
            if s1 == sorted(s2[l:r]):
                return True
            else:
                l = l + 1
                r = l + win
        return False