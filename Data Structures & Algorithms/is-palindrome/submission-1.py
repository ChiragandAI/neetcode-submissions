class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(ord("0"),ord("9"))
        all_char = set(range(ord("a"),ord("a")+26)).union(set(range(ord("0"),ord("0")+10)))
        s2 = ""
        for string in s.lower():
            if ord(string) in all_char:
                s2 += string
        print(s2.lower())
        print(s2.lower()[::-1])
        return s2.lower() == s2.lower()[::-1]