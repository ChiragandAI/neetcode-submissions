class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        count = 1
        best = 0
        for i in range(len(sorted_nums)):
            # print(sorted_nums[i],sorted_nums[i+1])
            if i < len(sorted_nums) -1:
                
                if sorted_nums[i]+1 == sorted_nums[i+1]:
                    count += 1
                else:
                    count = 1
            # print(count)
            best = max(count,best)
        return best
    #             # print(count)


                

