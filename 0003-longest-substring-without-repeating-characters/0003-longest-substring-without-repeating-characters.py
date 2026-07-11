class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # char -> most recent index
        left = 0
        best = 0

        for right, char in enumerate(s):
            # If char is inside the current window, shrink from the left
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            best = max(best, right - left + 1)

        return best