from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)

        # group indices by value
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        # precompute best[i] = min circular distance to nearest same-value index
        best = [-1] * n
        for idx_list in positions.values():
            if len(idx_list) < 2:
                continue  # unique value, stays -1
            m = len(idx_list)
            for k, i in enumerate(idx_list):
                # nearest neighbour is prev or next in the sorted list (circular)
                prev_i = idx_list[(k - 1) % m]
                next_i = idx_list[(k + 1) % m]

                d_prev = (i - prev_i) % n
                d_next = (next_i - i) % n

                best[i] = min(d_prev, d_next)

        return [best[q] for q in queries]