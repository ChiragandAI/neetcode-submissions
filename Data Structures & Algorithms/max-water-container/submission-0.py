class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights[::]
        l, r = 0, len(nums) - 1
        best = 0
        while l < r:
            area = (r-l)* min(nums[l],nums[r])
            best = max(area, best)
            if nums[l] > nums[r]:
                r -= 1
            else:
                l += 1
        return best