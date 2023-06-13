class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
 
        d = dict(sorted(d.items(),key = lambda x: x[1],reverse=True))
        return list(d.keys())[0]