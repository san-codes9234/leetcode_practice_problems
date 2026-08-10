class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        i0, i1 = x, x + k - 1

        while i0 < i1:
            for j in range(y, y + k):
                grid[i0][j], grid[i1][j] = grid[i1][j], grid[i0][j]
            i0 += 1
            i1 -= 1

        return grid
        