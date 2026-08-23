class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum_left = sum(int(c) for c in num[:half] if c != '?')
        sum_right = sum(int(c) for c in num[half:] if c != '?')
        q_left = num[:half].count('?')
        q_right = num[half:].count('?')

        # Bob wins iff: 2 * (sum_right - sum_left) == 9 * (q_left - q_right)
        return 2 * (sum_right - sum_left) != 9 * (q_left - q_right)