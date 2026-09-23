class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x  # find longest subarray with this sum

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        best = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                best = max(best, right - left + 1)

        return len(nums) - best if best != -1 else -1