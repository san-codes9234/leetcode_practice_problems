class Solution:
    def largestInteger(self, nums, k):
        count = {}

        # Consider every subarray of size k
        for i in range(len(nums) - k + 1):
            subarray = set(nums[i:i + k])

            # Each distinct number appears in this subarray
            for x in subarray:
                count[x] = count.get(x, 0) + 1

        ans = -1

        # Find the largest number appearing in exactly one subarray
        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans