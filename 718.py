class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lena, lenb = len(A), len(B)
        if lena == 0 or lenb == 0: return 0

        max = 0

        dp = [[0 for _ in range(lenb)] for _ in range(lena)]

        for i in range(lena):
            for j in range(lenb):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        if max < dp[i][j]:
                            max = dp[i][j]
                else:
                    dp[i][j] = 0

        return max
