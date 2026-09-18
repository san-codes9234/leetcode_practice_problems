class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: s.index(c) for c in set(s)}
        last  = {c: s.rindex(c) for c in set(s)}

        def get_interval(c: str) -> tuple[int, int]:
            """Expand interval for char c until stable."""
            lo, hi = first[c], last[c]
            i = lo
            while i <= hi:
                lo = min(lo, first[s[i]])
                if last[s[i]] > hi:
                    hi = last[s[i]]
                i += 1
            return lo, hi

        intervals = []
        for c in set(s):
            if first[c] == s.index(c):
                lo, hi = get_interval(c)
                if lo == first[c]:
                    intervals.append((hi, lo))

        intervals.sort()
        result = []
        prev_end = -1

        for hi, lo in intervals:
            if lo > prev_end:
                result.append(s[lo:hi+1])
                prev_end = hi

        return result