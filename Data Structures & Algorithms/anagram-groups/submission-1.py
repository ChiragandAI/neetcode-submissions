class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def anagram(s,t):
            if len(s) != len(t):
                return False
            seen = [0]*26
            for i,j in zip(s.lower(),t.lower()):
                seen[ord(i)-ord('a')] += 1
                seen[ord(j)-ord('a')] -= 1      

            for see in seen:
                if see != 0:
                  return False
            return True

        seen_list = [[strs[0]]]
        for string in strs[1:]:
            for final in range(len(seen_list)):
                result = anagram(seen_list[final][0],string)
                # print(result)
                if result:
                    seen_list[final].append(string)
                    break
            if not result: seen_list.append([string])
        return seen_list

