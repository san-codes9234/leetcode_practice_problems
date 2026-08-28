from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)

        odd_chars = [c for c, cnt in count.items() if cnt % 2 == 1]
        if len(odd_chars) > n % 2:
            return ""

        mid = odd_chars[0] if odd_chars else ""
        half_len = n // 2

        available = SortedList()
        for c, cnt in count.items():
            available.update([c] * (cnt // 2))

        def make_palindrome(h: list) -> str:
            h_str = "".join(h)
            return h_str + mid + h_str[::-1]

        prefix = []
        best = ""

        for i in range(half_len):
            t = target[i]

            idx = available.bisect_right(t)
            if idx < len(available):
                branch_char = available[idx]
                rest = list(available)
                rest.remove(branch_char)
                best = make_palindrome(prefix + [branch_char] + rest)

            if t in available:
                available.remove(t)
                prefix.append(t)
            else:
                break
        else:
            palindrome = make_palindrome(prefix)
            if palindrome > target:
                return palindrome 

        return best