from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        best = float('inf')
        for idx_list in indices.values():
            if len(idx_list) >= 3:
                for k in range(len(idx_list) - 2):
                    i, j, m = idx_list[k], idx_list[k+1], idx_list[k+2]
                    dist = abs(i-j) + abs(j-m) + abs(m-i)
                    best = min(best, dist)

        return best if best != float('inf') else -1