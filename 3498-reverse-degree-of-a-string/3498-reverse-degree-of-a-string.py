class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            reverse_pos = 27 - ord(c) + ord('a') - 1
            string_pos = i + 1
            total += reverse_pos * string_pos
        return total