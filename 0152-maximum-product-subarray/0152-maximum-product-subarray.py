# Runtime: 122 ms, faster than 48.40% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 15.7 MB, less than 5.47% of Python3 online submissions for Maximum Product Subarray.
class Solution:
    def maxProduct(self, nums):
        tempProMax, tempProMin = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        tempProMax[0] = tempProMin[0] = nums[0]
        for i in range(1, len(nums)):
            tempProMax[i] = max(tempProMax[i-1]*nums[i], tempProMin[i-1]*nums[i], nums[i])
            tempProMin[i] = min(tempProMax[i-1]*nums[i], tempProMin[i-1]*nums[i], nums[i])
        return max(tempProMax)