class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mx=nums.index(max(nums))
        mi=nums.index(min(nums))
        n=len(nums)
        if mi>mx:
            mi,mx=mx,mi
        return min(mx+1,n-mi,mi+1+n-mx)