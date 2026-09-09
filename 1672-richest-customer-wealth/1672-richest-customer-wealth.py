class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for i in accounts:
            s = sum(i)
            wealth.append(s)
        return max(wealth)