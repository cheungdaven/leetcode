class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or target == None:
            return False
        max_ids = {}
        for i in range(len(nums)):
            max_ids[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in max_ids and max_ids[target - nums[i]] != i :
                return [i, max_ids[target - nums[i]]]