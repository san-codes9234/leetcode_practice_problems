class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current_sum = 0
        
        for i in nums:
            current_sum += i
            result.append(current_sum)
        
        return result