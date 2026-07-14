from math import gcd

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 201   # nums[i] <= 200

        # dp[g1][g2] = ways to get (seq1 GCD=g1, seq2 GCD=g2) from elements seen so far
        # g=0 means that subsequence is still empty
        dp = [[0] * MAX_VAL for _ in range(MAX_VAL)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]    # copy handles the "skip x" case

            for g1 in range(MAX_VAL):
                for g2 in range(MAX_VAL):
                    if not dp[g1][g2]:
                        continue
                    w = dp[g1][g2]

                    # x joins seq1
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + w) % MOD

                    # x joins seq2
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + w) % MOD

            dp = new_dp

        # Both must be non-empty (g > 0) with equal GCDs
        return sum(dp[g][g] for g in range(1, MAX_VAL)) % MOD