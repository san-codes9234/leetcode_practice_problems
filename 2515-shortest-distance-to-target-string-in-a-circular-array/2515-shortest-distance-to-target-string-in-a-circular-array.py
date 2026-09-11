class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        best = float('inf')

        for i, word in enumerate(words):
            if word == target:
                forward = (i - startIndex) % n
                backward = (startIndex - i) % n
                best = min(best, forward, backward)

        return best if best != float('inf') else -1