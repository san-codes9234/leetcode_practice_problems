class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        for x in nums:
            xor ^= x
        
        if xor != 0:
            return len(nums)
        
        # Check if any non-zero element exists to remove
        for x in nums:
            if x != 0:
                return len(nums) - 1
        
        return 0