class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        best_start = [-1] * n

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    best_start[r] = max(best_start[r], l)
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)      # odd-length
            expand(i, i + 1)  # even-length

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            e = i - 1
            dp[i] = dp[i - 1]
            if best_start[e] != -1:
                dp[i] = max(dp[i], dp[best_start[e]] + 1)

        return dp[n]