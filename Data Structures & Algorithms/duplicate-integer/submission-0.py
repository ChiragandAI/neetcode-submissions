class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        res = False
        for num in nums:
            if num in count:
                count[num] = count[num] + count.get(num,1)
            else:
                count.setdefault(num,1)
            if count[num] > 1:
                res = True
                break
        return res