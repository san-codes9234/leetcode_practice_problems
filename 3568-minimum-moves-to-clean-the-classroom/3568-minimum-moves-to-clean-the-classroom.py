from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter_cells = {}
        sr = sc = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_cells[(r, c)] = len(litter_cells)

        total_litter = len(litter_cells)
        full_mask = (1 << total_litter) - 1

        best_energy = [[[- 1] * (full_mask + 1) for _ in range(n)] for _ in range(m)]
        best_energy[sr][sc][0] = energy

        queue = deque([(0, sr, sc, 0, energy)])

        while queue:
            moves, r, c, mask, e = queue.popleft()

            if mask == full_mask:
                return moves

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue

                    new_mask = mask
                    if (nr, nc) in litter_cells:
                        new_mask |= (1 << litter_cells[(nr, nc)])

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    if ne > best_energy[nr][nc][new_mask]:
                        best_energy[nr][nc][new_mask] = ne
                        queue.append((moves + 1, nr, nc, new_mask, ne))

        return -1