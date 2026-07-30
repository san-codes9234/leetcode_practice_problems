class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        for i, _ in enumerate(word):
            total += (i // 8) + 1
        return total