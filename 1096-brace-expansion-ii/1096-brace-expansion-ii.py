class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        result = self.parse_expression(expression)
        return sorted(list(result))

    def parse_expression(self, s: str) -> set[str]:
        # Union level (handles ',')
        res = self.parse_term(s)
        while self.i < len(s) and s[self.i] == ',':
            self.i += 1  # skip ','
            res |= self.parse_term(s)
        return res

    def parse_term(self, s: str) -> set[str]:
        # Concatenation level
        res = {""}
        while self.i < len(s) and (s[self.i].isalpha() or s[self.i] == '{'):
            next_factor = self.parse_factor(s)
            res = {a + b for a in res for b in next_factor}
        return res

    def parse_factor(self, s: str) -> set[str]:
        # Base units: individual characters or sub-expressions in braces
        if s[self.i] == '{':
            self.i += 1  # skip '{'
            res = self.parse_expression(s)
            self.i += 1  # skip '}'
            return res
        else:
            ch = s[self.i]
            self.i += 1
            return {ch}

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna