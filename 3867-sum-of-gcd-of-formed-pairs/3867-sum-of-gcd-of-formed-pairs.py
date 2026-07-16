from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        running_max = 0

        for num in nums:
            if num > running_max:
                running_max = num
            prefix_gcd.append(gcd(num, running_max))

        prefix_gcd.sort()

        total = 0
        left = 0
        right = len(prefix_gcd) - 1
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return total