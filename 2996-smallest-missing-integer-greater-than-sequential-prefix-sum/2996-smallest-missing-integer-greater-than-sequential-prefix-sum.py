class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # step 1: find the sum of the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # step 2: find smallest missing integer >= total
        nums_set = set(nums)
        while total in nums_set:
            total += 1

        return total