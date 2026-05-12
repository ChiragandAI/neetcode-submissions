class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in seen:
                return [seen[compliment]+1,i+1]
            seen[numbers[i]] = i
        return -1