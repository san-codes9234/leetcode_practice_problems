class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            ones += int(s[right])

            # shrink from left while we have exactly k ones
            # (to find the shortest window with exactly k ones)
            while ones == k and s[left] == '0':
                left += 1

            if ones == k:
                window = s[left:right + 1]
                if not best or len(window) < len(best) or \
                   (len(window) == len(best) and window < best):
                    best = window
                left += 1   # move past this window's leading '1'
                ones -= 1

        return best