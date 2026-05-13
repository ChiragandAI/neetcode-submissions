class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mx:
                l = max(mx[s[r]]+1,l)
            mx[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
