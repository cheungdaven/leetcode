class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid:
        List[List[int]]

    ) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if n == 0 or obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = 0 if obstacleGrid[0][i] == 1 else dp[i - 1]
    print(dp)
    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            dp[0] = 0
        for j in range(1, n):
            dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j - 1] + dp[j]

    print(dp)
    return dp[n - 1]