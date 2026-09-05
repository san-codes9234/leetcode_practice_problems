class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        pmax = [0] * n
        pmax[0] = nums[0]
        for i in range(1, n):
            pmax[i] = max(pmax[i-1], nums[i])
        
        smin = [0] * n
        smin[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            smin[i] = min(smin[i+1], nums[i])
        
        for i in range(n):
            if pmax[i] - smin[i] <= k:
                return i
        
        return -1