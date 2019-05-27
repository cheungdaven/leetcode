class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        dp = [1 for _ in range(len(nums))]
        res = {}
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1 )
        print(dp)
        res = self.generateLIS(nums, dp)
        return max(dp), res

    def generateLIS(self, arr, dp):
        n = max(dp)
        index = dp.index(n)
        lis = [0] * n
        n -= 1
        lis[n] = arr[index]
        # 从右向左
        for i in range(index, 0 - 1, -1):
            # 关键
            if arr[i] < arr[index] and dp[i] == dp[index] - 1:
                n -= 1
                lis[n] = arr[i]
                index = i
        return lis

def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    print(m)
    return result


arr = "ascdsfasfafa"
print(lis(arr))

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS("ascdsfasfafa"))