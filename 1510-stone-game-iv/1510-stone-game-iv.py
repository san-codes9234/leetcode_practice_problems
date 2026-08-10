class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if the current player wins with i stones
        dp = [False] * (n + 1)
        # dp[0] = False: no moves available, current player loses

        for i in range(1, n + 1):
            s = 1
            while s * s <= i:
                if not dp[i - s * s]:   # opponent loses from that state
                    dp[i] = True
                    break               # found a winning move, no need to check more
                s += 1

        return dp[n]