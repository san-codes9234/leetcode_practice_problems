class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with the low pointer element
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in the right place (middle), just move the scanner
                mid += 1
            else:  # nums[mid] == 2
                # Swap current element with the high pointer element
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1