from sortedcontainers import SortedList
import bisect

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        available = SortedList(s)
        n = len(s)
        prefix = []
        best = ""

        for i in range(n):
            t = target[i]

            # find smallest char strictly greater than target[i]
            idx = available.bisect_right(t)
            if idx < len(available):
                # candidate: current prefix + that char + rest sorted ascending
                branch_char = available[idx]
                rest = list(available)
                rest.remove(branch_char)
                candidate = "".join(prefix) + branch_char + "".join(rest)
                best = candidate  # overwrite — later positions give smaller results

            # try to match target[i] exactly and continue
            if t in available:
                available.remove(t)
                prefix.append(t)
            else:
                break   # can't match — no further branching possible

        return best