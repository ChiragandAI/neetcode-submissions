
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        target = k
        count = {}
        lst = [[] for i in range(len(nums)+1)]
        # print(lst)
        for num in nums:
            count[num] = 1 + count.get(num,0)
        # print(count)
        for k,v in count.items():
            lst[v].append(k)
        # print(lst)
        res = []
        for el in lst[::-1]:
            for e in el:
                if e == []: continue
                res.append(e)
                # print(res,len(res),"this is k: ",k)
                if len(res) == target:
                    # print("I'm in")
                    return res