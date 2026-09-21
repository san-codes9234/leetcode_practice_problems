class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at current index with product ≡ r (mod k)
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # extend all previous subarrays by num
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            # single-element subarray [num]
            new_dp[num % k] += 1

            dp = new_dp

            # accumulate into result
            for r in range(k):
                result[r] += dp[r]

        return result