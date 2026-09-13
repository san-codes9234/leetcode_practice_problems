class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        best = 0

        for dr in range(-(n-1), n):
            for dc in range(-(n-1), n):
                count = 0
                for r in range(n):
                    for c in range(n):
                        r2, c2 = r + dr, c + dc
                        if 0 <= r2 < n and 0 <= c2 < n:
                            if img1[r][c] == 1 and img2[r2][c2] == 1:
                                count += 1
                best = max(best, count)

        return best