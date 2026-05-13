class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        # print(f"sorted nums: {nums}")
        for idx, el in enumerate(nums):
            if el > 0:
                break
            if idx > 0 and el == nums[idx-1]:
                continue
            l, r = idx + 1,len(nums) - 1
            # print(f"el: {el}, idx: {idx}, l: {l}, r: {r}")
            while l < r:
                # print(f"in while, l: {l}, r: {r}")
                if el + nums[l] + nums[r] < 0:
                    # print(f"chota, {nums[l]} + {nums[r]} < {el}")
                    l += 1
                elif el + nums[l] + nums[r] > 0:
                    # print(f"bada, {nums[l]} + {nums[r]} > {el}")
                    r -= 1
                else:
                    
                    sol.append([el,nums[l],nums[r]])
                    # print("mil gaya")
                    # print(f"sol: {sol}")/
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        # print(f"final sol: {sol}")
        return sol
            

            