class Solution(object):
    def findDuplicates(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        a = []
        for i in d.keys():
            if d[i] > 1:
                a.append(i)
        return sorted(a)