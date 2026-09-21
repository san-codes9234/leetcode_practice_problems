class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k

        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            new_dp[num % k] += 1

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result