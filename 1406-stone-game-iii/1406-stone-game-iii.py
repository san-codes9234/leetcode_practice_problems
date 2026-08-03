class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s1, s2, s3 = 0, 0, 0
        tot = 0

        for value in reversed(stoneValue):
            tot += value
            s1, s2, s3 = tot-min(s1,s2,s3),s1,s2
        bob = tot - s1
        if s1 > bob:
            return "Alice"
        elif s1 < bob:
            return "Bob"
        else:
            return "Tie"
        