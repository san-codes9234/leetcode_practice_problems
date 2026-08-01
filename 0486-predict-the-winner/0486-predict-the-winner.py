class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        # dp[i][j] = max score advantage the current player can get over opponent in nums[i..j]
        dp = [[0] * n for _ in range(n)]

        # base case: only one element, current player takes it all
        for i in range(n):
            dp[i][i] = nums[i]

        # fill by increasing subarray length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],  # take left end
                    nums[j] - dp[i][j - 1]   # take right end
                )

        return dp[0][n - 1] >= 0