class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i,j in zip(s,t):
            seen[i] = seen.get(i,0) + 1
            seen[j] = seen.get(j,0) - 1
        for k,v in seen.items():
            if v != 0:
                return False
        return True