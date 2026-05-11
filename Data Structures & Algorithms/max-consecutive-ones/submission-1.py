class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = -1
        count = 0
        for i,num in enumerate(nums):
            if num == 1:
                count += 1
                # print(f"num: {num}\n count: {count}")
            else:
                count = 0
                # print(f"num: {num}\n count: {count}")
            if count >= best:
                best = count
        return best