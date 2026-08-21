from math import gcd, lcm
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # remove redundant coins: if coin b is a multiple of coin a,
        # every multiple of b is already covered by a → drop b
        coins = [c for c in coins if not any(c != d and c % d == 0 for d in coins)]

        n = len(coins)

        def count(x: int) -> int:
            """Count how many distinct multiples of at least one coin are <= x."""
            total = 0
            # inclusion-exclusion over all non-empty subsets
            for size in range(1, n + 1):
                for subset in combinations(coins, size):
                    l = subset[0]
                    for c in subset[1:]:
                        l = lcm(l, c)
                        if l > x:   # lcm exceeds x, contributes 0
                            break
                    else:
                        # inclusion-exclusion: add for odd size, subtract for even
                        if size % 2 == 1:
                            total += x // l
                        else:
                            total -= x // l
            return total

        # binary search: find smallest x where count(x) >= k
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo