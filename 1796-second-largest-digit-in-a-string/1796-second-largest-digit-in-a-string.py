class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for char in s:
            if char.isdigit():
                digits.append(int(char))
        unique = sorted(set(digits))
        if len(unique) < 2:
            return -1
        return unique[-2]