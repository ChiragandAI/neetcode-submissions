class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        def mul(lst):
            ans = 1
            for i in lst:
                ans *= i
            # print(ans)
            return ans
        for i in range(len(nums)):
            temp =  mul(nums[:i]) * mul(nums[i+1:])
            new.append(temp)
        # print(new)
        return new
            