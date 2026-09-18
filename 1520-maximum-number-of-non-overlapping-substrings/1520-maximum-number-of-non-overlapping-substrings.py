class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # step 1: find first and last occurrence of each character
        first = {c: s.index(c) for c in set(s)}
        last  = {c: s.rindex(c) for c in set(s)}

        def get_interval(c: str) -> tuple[int, int]:
            """Expand interval for char c until stable."""
            lo, hi = first[c], last[c]
            i = lo
            while i <= hi:
                # if char at i has occurrences outside [lo,hi], expand
                lo = min(lo, first[s[i]])
                if last[s[i]] > hi:
                    hi = last[s[i]]
                    # restart scan won't miss anything since lo only shrinks left
                i += 1
            return lo, hi

        # step 2: compute valid intervals for each unique character
        intervals = []
        for c in set(s):
            if first[c] == s.index(c):  # only process each char once from its first pos
                lo, hi = get_interval(c)
                # valid only if the interval starts at first[c]
                # (if lo != first[c], this char is subsumed by another)
                if lo == first[c]:
                    intervals.append((hi, lo))

        # step 3: greedy — sort by end, pick non-overlapping (classic interval scheduling)
        intervals.sort()
        result = []
        prev_end = -1

        for hi, lo in intervals:
            if lo > prev_end:
                result.append(s[lo:hi+1])
                prev_end = hi

        return result