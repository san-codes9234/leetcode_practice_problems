class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        half = total // 2

        # check horizontal cuts
        prefix = 0
        for i in range(len(grid) - 1):       # cut after row i, row i+1 must exist
            prefix += sum(grid[i])
            if prefix == half:
                return True

        # check vertical cuts
        prefix = 0
        for j in range(len(grid[0]) - 1):    # cut after col j, col j+1 must exist
            prefix += sum(row[j] for row in grid)
            if prefix == half:
                return True

        return False