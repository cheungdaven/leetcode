class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, curMin, curMax = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            curMax, curMin = curMax * nums[i], curMin * nums[i]
            curMax, curMin = max(curMax, curMin, nums[i]), min(curMin, curMax, nums[i])
            res = curMax if curMax > res  else res
        return res