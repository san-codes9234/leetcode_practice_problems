class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer to place the next element that is NOT equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the valid element forward
                k += 1             # Increment the count of valid elements
                
        return k
        