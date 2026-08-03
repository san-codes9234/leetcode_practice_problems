class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] = max score advantage current player can get from index i onwards
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # base case: no stones left, no advantage

        # build suffix sums for quick range sum calculation
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]

        for i in range(n - 1, -1, -1):
            for take in range(1, 4):  # take 1, 2, or 3 stones
                if i + take <= n:
                    stones_taken = suffix[i] - suffix[i + take]
                    dp[i] = max(dp[i], stones_taken - dp[i + take])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"