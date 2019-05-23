class Solution(object):
    '''
    complexity nlog(n)
    '''

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        l = len(nums)
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = l - 1
            j = i + 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
        return res