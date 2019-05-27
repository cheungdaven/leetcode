class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        len_tri = len(triangle)
        dp = [[0 for _ in triangle[i]] for i in range(len_tri)]
        dp[len_tri - 1] = triangle[len_tri - 1]
        for m in range(len_tri - 2, -1, -1):
            for j in range(len(triangle[m])):
                dp[m][j] = min(dp[m+1][j], dp[m+1][j+1]) + triangle[m][j]
        return dp[0][0]