from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        best = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            # shrink window from left until the window is good again
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best