class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        return [n for n in range(min(nums), max(nums) + 1) if n not in nums_set]