class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m

        # Flatten grid into 1D for easier indexing
        flat = [grid[i][j] % MOD for i in range(n) for j in range(m)]

        p = [1] * total

        # Forward pass: p[k] = product of flat[0..k-1]
        prefix = 1
        for k in range(total):
            p[k] = prefix
            prefix = prefix * flat[k] % MOD

        # Backward pass: multiply p[k] by product of flat[k+1..end]
        suffix = 1
        for k in range(total - 1, -1, -1):
            p[k] = p[k] * suffix % MOD
            suffix = suffix * flat[k] % MOD

        # Reshape back to 2D
        return [[p[i * m + j] for j in range(m)] for i in range(n)]