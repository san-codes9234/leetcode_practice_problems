class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        lo = nums.index(min(nums))
        hi = nums.index(max(nums))

        lo, hi = min(lo, hi), max(lo, hi)

        return min(hi + 1, n - lo, (lo + 1) + (n - hi))